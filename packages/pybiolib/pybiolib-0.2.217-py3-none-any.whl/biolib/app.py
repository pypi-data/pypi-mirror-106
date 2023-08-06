# Importing ascii is necessary for file open to work in some environments
from queue import Queue
import platform
from encodings import ascii  # pylint: disable=redefined-builtin, unused-import
from pathlib import Path
import http.server
import asyncio
import base64
import logging
import os
import re
import shutil
import signal
import socketserver
import subprocess
import sys
import tempfile
import threading
from json.decoder import JSONDecodeError
import nest_asyncio  # necessary import fix required for async to work in notebooks
import requests
import yaml
from biolib import cli_utils
from biolib.biolib_binary_format import ModuleInput, ModuleOutput
from biolib.compute_node.compute_process.biolib_container import BiolibContainer
from biolib.pyppeteer.pyppeteer import launch, command
from biolib.pyppeteer.pyppeteer.launcher import resolveExecutablePath, __chromium_revision__
from biolib.compute_node.compute_process.compute_process import ComputeProcess
from biolib.biolib_docker_client import BiolibDockerClient

if platform.system() != 'Windows':
    from biolib.compute_node.webserver import webserver

nest_asyncio.apply()

logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                    level=logging.INFO, stream=sys.stdout)
logging.getLogger('biolib.pyppeteer.pyppeteer').setLevel(logging.ERROR)
logging.getLogger('biolib.pyppeteer.pyppeteer.connection').setLevel(logging.ERROR)

biolib_logger = logging.getLogger('biolib')


class BioLibError(Exception):
    # pylint: disable=super-init-not-called
    def __init__(self, message):
        self.message = message


class CompletedProcess:
    def __init__(self, stdout, stderr, exitcode):
        self.stdout = stdout
        self.stderr = stderr
        self.exitcode = exitcode

    def ipython_markdown(self):
        from IPython.display import display, Markdown  # pylint: disable=import-error, import-outside-toplevel
        markdown_str = self.stdout.decode('utf-8')
        # prepend ./biolib_results/ to all paths
        # ie [SeqLogo](./SeqLogo2.png) test ![SeqLogo](./SeqLogo.png)
        # ![SeqLogo](SeqLogo.png)  ![SeqLogo](/SeqLogo.png)
        # is transformed to ![SeqLogo](./biolib_results/SeqLogo2.png) test ![SeqLogo](./biolib_results/SeqLogo.png)
        # ![SeqLogo](./biolib_results/SeqLogo.png)  ![SeqLogo](./biolib_results/SeqLogo.png)
        markdown_str_modified = re.sub(r'\!\[([^\]]*)\]\((\.\/|\/|)([^\)]*)\)',
                                       r'![\\1](./biolib_results/\\3)',
                                       markdown_str)
        display(Markdown(markdown_str_modified))


class BioLibServer(socketserver.TCPServer):
    log_level = logging.INFO


class BioLibHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):  # pylint: disable=redefined-builtin
        if self.server.log_level == BioLib.TRACE_LOGGING:
            http.server.SimpleHTTPRequestHandler.log_message(self, format, *args)


def js_to_python_byte_array_converter(js_encoded):
    try:
        return bytes(list([js_encoded[str(i)] for i in range(len(js_encoded))]))
    except Exception as error:
        biolib_logger.error("Failed to decode response from browser")
        biolib_logger.error(error)
        biolib_logger.error(js_encoded)
        raise BioLibError(js_encoded) from error


def python_bytes_to_byte64(data):
    return base64.b64encode(data).decode('ascii')


class BioLib:
    executable_path = None
    no_sandbox = True
    log_level = logging.INFO
    TRACE_LOGGING = 50
    auth_api_token = None
    auth_access_token = None
    auth_refresh_token = None
    host = 'https://biolib.com'

    @staticmethod
    def set_chrome_path(path):
        BioLib.executable_path = path

    @staticmethod
    def set_sandbox(use_sandbox):
        BioLib.no_sandbox = not use_sandbox

    @staticmethod
    def set_api_token(api_token):
        BioLib.auth_api_token = api_token

    @staticmethod
    def attempt_login(exit_on_failure=False):
        if BioLib.auth_api_token is None:
            if exit_on_failure:
                biolib_logger.error('Error: Attempted login, but BIOLIB_TOKEN was not set, exiting...')
                sys.exit(1)
            else:
                biolib_logger.debug('Attempted login, but BIOLIB_TOKEN was not set, so continuing without logging in')
                return

        response = requests.post(f'{BioLib.host}/api/user/api_tokens/exchange/',
                                 json={'token': BioLib.auth_api_token})
        try:
            json_response = response.json()
        except JSONDecodeError:
            biolib_logger.error('Could not decode response from server as JSON:')
            biolib_logger.error(response.text)
            sys.exit(1)
        if not response.ok:
            biolib_logger.error('Login with API token failed:')
            biolib_logger.error(json_response['detail'])
            sys.exit(1)
        else:
            BioLib.auth_refresh_token = json_response['refresh_token']
            BioLib.auth_access_token = json_response['access_token']
            biolib_logger.info('Successfully authenticated')

    @staticmethod
    def push(author_and_app_name, app_path):
        # prepare zip file
        if not Path(f'{app_path}/.biolib/config.yml').is_file():
            biolib_logger.error('The file .biolib/config.yml was not found in the application directory')
            sys.exit(1)
        cwd = os.getcwd()
        temp_dir = tempfile.TemporaryDirectory()
        os.chdir(app_path)
        try:
            zip_path_without_file_extension = os.path.join(temp_dir.name, 'biolib-cli-build-tmp-zip')
            zip_path = f'{zip_path_without_file_extension}.zip'
            app_folder_name = Path(app_path).absolute().parts[-1]
            shutil.make_archive(zip_path_without_file_extension, 'zip', root_dir='..', base_dir=app_folder_name)
            zip_file = open(zip_path, 'rb')
            zip_binary = zip_file.read()
            zip_file.close()
        except Exception as error:
            raise Exception("Failed to create zip of application") from error
        finally:
            temp_dir.cleanup()
            # change back to old working directory
            os.chdir(cwd)

        # login and get app data
        BioLib.attempt_login(exit_on_failure=True)
        author_and_app_name_split = author_and_app_name.split('/')
        app = BioLib.get_app_from_author_and_app_name(author_and_app_name_split[0],
                                                      author_and_app_name_split[1])
        # push new app version
        response = requests.post(
            f'{BioLib.host}/api/app_versions/',
            headers={'Authorization': f'Bearer {BioLib.auth_access_token}'},
            files={
                'app': (None, app['public_id']),
                'set_as_active': (None, 'true'),
                'state': (None, 'published'),
                'source_files_zip': zip_binary
            })
        if not response.ok:
            biolib_logger.error(f'Push failed for {author_and_app_name}:')
            biolib_logger.error(response.text)
            sys.exit(1)
        else:
            # TODO: When response includes the version number, print the URL for the new app version
            json_response = response.json()
            biolib_logger.info(f'Successfully pushed app version for {author_and_app_name}.')

        docker_tags = json_response.get('docker_tags', {})
        if docker_tags:
            biolib_logger.info('Found docker images to push.')

            try:
                yaml_file = open(f'{app_path}/.biolib/config.yml', 'r', encoding='utf-8')

            except Exception as error:  # pylint: disable=broad-except
                biolib_logger.debug(error)
                biolib_logger.error('Could not open the config file .biolib/config.yml')
                sys.exit(1)

            try:
                config_data = yaml.safe_load(yaml_file)

            except Exception as error:  # pylint: disable=broad-except
                biolib_logger.debug(error)
                biolib_logger.error('Could not parse .biolib/config.yml. Please make sure it is valid YAML')
                sys.exit(1)

            # Auth to be sent to proxy
            # The tokens are sent as "{access_token},{job_id}". We leave job_id blank on push.
            tokens = f'{BioLib.auth_access_token},'
            auth_config = {'username': 'biolib', 'password': tokens}

            docker_client = BiolibDockerClient.get_docker_client()

            for module_name, repo_and_tag in docker_tags.items():
                docker_image_definition = config_data['modules'][module_name]['image']
                repo, tag = repo_and_tag.split(':')

                if docker_image_definition.startswith('dockerhub://'):
                    docker_image_name = docker_image_definition.replace('dockerhub://', 'docker.io/', 1)
                    biolib_logger.info(
                        f'Pulling image {docker_image_name} defined on module {module_name} from Dockerhub.')
                    dockerhub_repo, dockerhub_tag = docker_image_name.split(':')
                    docker_client.images.pull(dockerhub_repo, tag=dockerhub_tag)

                elif docker_image_definition.startswith('local-docker://'):
                    docker_image_name = docker_image_definition.replace('local-docker://', '', 1)

                try:
                    biolib_logger.info(f'Trying to push image {docker_image_name} defined on module {module_name}.')
                    image = docker_client.images.get(docker_image_name)
                    ecr_proxy_host = f'containers.{BioLib.host.split("://")[1]}/{repo}'
                    image.tag(ecr_proxy_host, tag)
                    for line in docker_client.images.push(ecr_proxy_host, tag=tag, stream=True,
                                                          decode=True, auth_config=auth_config):
                        biolib_logger.info(line)

                except Exception as exception:  # pylint: disable=broad-except
                    biolib_logger.debug(exception)
                    biolib_logger.error(f'Failed to tag and push image {docker_image_name}.')
                    sys.exit(1)

                biolib_logger.info(f'Successfully pushed {docker_image_name}')

            biolib_logger.info('Successfully pushed all docker images')

    @staticmethod
    def build_enclave(dev_mode):
        compute_node_dir = f'{BioLib.get_pybiolib_root()}/biolib/compute_node'
        output_eif_path = f'{os.getcwd()}/biolib-nitro-enclave.eif'

        if os.path.exists(output_eif_path):
            os.remove(output_eif_path)

        if dev_mode:
            pybiolib_tar_path = f'{BioLib.get_pybiolib_root()}/biolib/compute_node/enclave_build/pybiolib-0.0.1.tar.gz'
            if os.path.exists(pybiolib_tar_path):
                os.remove(pybiolib_tar_path)

            cur_dir = os.getcwd()
            os.chdir(BioLib.get_pybiolib_root())
            subprocess.run(['poetry', 'build'], check=True)
            shutil.move('./dist/pybiolib-0.0.1.tar.gz', pybiolib_tar_path)
            os.chdir(cur_dir)

            subprocess.run(
                ['sudo', 'docker', 'build', f'{compute_node_dir}/enclave_build/', '-t', 'biolib-nitro-enclave',
                 '--build-arg', 'ENV=dev'],
                check=True)
        else:
            subprocess.run(
                ['sudo', 'docker', 'build', f'{compute_node_dir}/enclave_build/', '-t', 'biolib-nitro-enclave'],
                check=True)

        subprocess.run(
            ['sudo', 'nitro-cli', 'build-enclave', '--docker-uri', 'biolib-nitro-enclave:latest', '--output-file',
             output_eif_path],
            check=True)

    @staticmethod
    def start_compute_node(port, host, eif_path=None):
        if platform.system() == 'Windows':
            biolib_logger.error('Starting a compute node is currently not supported on Windows')
            sys.exit(1)
        webserver.start_webserver(port=port, host=host, specified_biolib_host=BioLib.host, specified_eif_path=eif_path)

    @staticmethod
    def start_compute_process(socket_port, is_running_in_enclave):
        ComputeProcess(socket_port, is_running_in_enclave).run()
        # Kill the compute process which is the current process
        os.kill(os.getpid(), signal.SIGKILL)

    @staticmethod
    def run_local_docker_app(input_files, args, module, source_files_temp_dir):
        error_queue = Queue()
        biolib_container = BiolibContainer(is_running_in_enclave=False, messages_to_send_queue=error_queue)
        biolib_container.initialize_docker_container(
            image=module["image"],
            command=f'{module["command"]} {" ".join(args)}',
            working_dir=module['working_directory']
        )

        biolib_container.set_mappings(
            module['input_files_mappings'],
            module['source_files_mappings'],
            module['output_files_mappings'],
            args
        )

        if input_files:
            biolib_container.map_and_copy_input_files_to_container(input_files)

        if source_files_temp_dir:
            runtime_zip_data = open(f'{source_files_temp_dir.name}/biolib_run_dev.zip', 'rb').read()
            biolib_container.map_and_copy_runtime_files_to_container(runtime_zip_data, remove_root_folder=False)

        stdout, stderr, exit_code, mapped_output_files = biolib_container.run()
        cli_utils.return_results(stdout, stderr, exit_code, mapped_output_files)

        biolib_container.cleanup()


    @staticmethod
    def get_app_from_author_and_app_name(author_name, app_name):
        headers = {}
        if BioLib.auth_access_token is not None:
            headers['Authorization'] = f'Bearer {BioLib.auth_access_token}'
        apps_response = requests.get(f'{BioLib.host}/api/apps/?account_handle={author_name}&app_name={app_name}',
                                     headers=headers)
        results = apps_response.json()['results']
        if len(results) == 0:
            raise Exception(f'Application "{author_name}/{app_name}" was not found. '
                            f'Make sure you have spelled the application name correctly, '
                            f'and that you have the required permissions.')
        return results[0]

    @staticmethod
    def get_pybiolib_root():
        # Use dirname() twice to get pybiolib/ as __file__ pybiolib/biolib/app.py
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    @staticmethod
    def set_logging(log_level):
        BioLib.log_level = log_level
        # only activate debug logging globally if user selected trace logging
        if log_level == BioLib.TRACE_LOGGING:
            logging.getLogger().setLevel(logging.DEBUG)
        elif log_level == logging.DEBUG:
            logging.getLogger().setLevel(logging.INFO)
            biolib_logger.setLevel(logging.DEBUG)
        else:
            logging.getLogger().setLevel(log_level)

    @staticmethod
    def set_host(host):
        if host:
            BioLib.host = host


# set default logging to info
BioLib.set_logging(logging.INFO)


class BioLibApp:
    app_author = None
    app_name = None

    def __init__(self, author, name):
        self.app_author = author
        self.app_name = name
        self.app_version_public_id = None

    async def call_pyppeteer(self, port, args, stdin, files, output_dir_path):
        if not BioLib.executable_path:
            mac_chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
            if os.path.isfile(mac_chrome_path):
                BioLib.set_chrome_path(mac_chrome_path)

        if not BioLib.executable_path:
            linux_chrome_path = '/usr/lib/chromium-browser/chromium-browser'

            # special install for google colab
            if not os.path.isfile(linux_chrome_path) and 'google.colab' in sys.modules:
                subprocess.run('apt-get update', shell=True, check=True)
                subprocess.run('apt install chromium-chromedriver', shell=True, check=True)

            if os.path.isfile(linux_chrome_path):
                BioLib.set_chrome_path(linux_chrome_path)

        resolved_path = resolveExecutablePath(None, __chromium_revision__)
        if not BioLib.executable_path and resolved_path[1]:
            # if executable_path is not set explicit,
            # and resolveExecutablePath failed (== we got an error message back in resolved_path[1])
            logging.info('Installing dependencies...')
            os.environ['PYPPETEER_NO_PROGRESS_BAR'] = 'true'
            command.install()

        logging.info('Computing...')

        chrome_arguments = [
            '--disable-web-security',
        ]
        if BioLib.no_sandbox:
            chrome_arguments.append('--no-sandbox')

        browser = await launch(args=chrome_arguments, executablePath=BioLib.executable_path)

        # start new page
        page = await browser.newPage()

        await page.goto('http://localhost:' + str(port))

        def get_data():
            input_serialized = ModuleInput().serialize(stdin, args, files)
            return python_bytes_to_byte64(input_serialized)

        def set_progress_compute(value):
            biolib_logger.debug(f'Compute progress: {value}')

        def set_progress_initialization(value):
            biolib_logger.debug(f'Initialization progress: {value}')

        def add_log_message(value):
            biolib_logger.debug(f'Log message: {value}')

        await page.exposeFunction('getData', get_data)
        await page.exposeFunction('setProgressCompute', set_progress_compute)
        await page.exposeFunction('setProgressInitialization', set_progress_initialization)
        await page.exposeFunction('addLogMessage', add_log_message)

        refresh_token = 'undefined'
        if BioLib.auth_refresh_token:
            refresh_token = f'\'{BioLib.auth_refresh_token}\''

        output_serialized_js_bytes = await page.evaluate('''
        async function() {
          const refreshToken = ''' + refresh_token + ''';
          const appVersionId = \'''' + self.app_version_public_id + '''\';
          const baseUrl = \'''' + BioLib.host + '''\';

          const { BioLibSingleton, AppClient } = window.BioLib;
          BioLibSingleton.setConfig({ baseUrl, refreshToken });
          AppClient.setApiClient(BioLibSingleton.get());

          const inputBase64 = await window.getData();
          const inputByteArray = Uint8Array.from(atob(inputBase64), c => c.charCodeAt(0));

          const jobUtils = {
              setProgressCompute: window.setProgressCompute,
              setProgressInitialization: window.setProgressInitialization,
              addLogMessage: window.addLogMessage,
          };

          try {
            const moduleOutput = await AppClient.runAppVersion(appVersionId, inputByteArray, jobUtils);
            return moduleOutput.serialize();
          } catch(err) {
            return err.toString();
          }
        }
        ''')
        logging.debug('Closing browser')
        await browser.close()

        output_serialized = js_to_python_byte_array_converter(output_serialized_js_bytes)
        output = ModuleOutput(output_serialized).deserialize()

        if isinstance(output, dict):
            if len(output['files']) > 0:
                logging.info(f'Writing output files to: {output_dir_path}')

                for file_path, data in output['files'].items():
                    full_path = output_dir_path + file_path

                    if full_path.endswith('/'):
                        path_without_file_name = full_path
                        filename = ''
                    else:
                        full_path_parts = full_path.split('/')
                        filename = full_path_parts.pop()
                        path_without_file_name = '/'.join(full_path_parts) + '/'

                    os.makedirs(path_without_file_name, exist_ok=True)

                    if filename != '':
                        output_file = open(path_without_file_name + filename, 'wb')
                        output_file.write(data)
                        output_file.close()

            return CompletedProcess(stdout=output['stdout'], stderr=output['stderr'], exitcode=output['exit_code'])
        else:
            raise BioLibError(output)

    def __call__(self, args=None, stdin=None, files=None, output_path='biolib_results'):
        if args is None:
            args = []
        BioLib.attempt_login()
        logging.info('Loading package...')
        app = BioLib.get_app_from_author_and_app_name(self.app_author, self.app_name)
        active_version = app['active_version']
        self.app_version_public_id = active_version['public_id']

        logging.info(f'Loaded package: {self.app_author}/{self.app_name}')

        cwd = os.getcwd()

        if stdin is None:
            stdin = b''

        if not output_path.startswith('/'):
            # output_path is relative, make absolute
            output_path = f'{cwd}/{output_path}'

        if isinstance(args, str):
            args = list(filter(lambda p: p != '', args.split(' ')))

        if not isinstance(args, list):
            raise Exception('The given input arguments must be list or str')

        if isinstance(stdin, str):
            stdin = stdin.encode('utf-8')

        if files is None:
            files = []
            for idx, arg in enumerate(args):
                if os.path.isfile(arg):
                    files.append(arg)
                    args[idx] = arg.split('/')[-1]

        files_dict = {}

        for file in files:
            path = file
            if not file.startswith('/'):
                # make path absolute
                path = cwd + '/' + file

            arg_split = path.split('/')
            file = open(path, 'rb')
            path = '/' + arg_split[-1]

            files_dict[path] = file.read()
            file.close()

        BioLibServer.log_level = BioLib.log_level
        with BioLibServer(('127.0.0.1', 0), BioLibHandler) as httpd:
            port = httpd.server_address[1]
            thread = threading.Thread(target=httpd.serve_forever)
            # TODO: figure out how we can avoid changing the current directory
            os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/biolib-js/')
            try:
                thread.start()
                res = asyncio.get_event_loop().run_until_complete(
                    self.call_pyppeteer(port=port, args=args, stdin=stdin, files=files_dict,
                                        output_dir_path=output_path))
            finally:
                os.chdir(cwd)
                httpd.shutdown()
                thread.join()
            return res

        raise BioLibError('Failed to start TCPServer')
