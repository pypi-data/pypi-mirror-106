import os
import yaml
import json
import requests
import traceback
import boto3
import subprocess
import shlex
from typing import Any, Dict
from typing_extensions import TypedDict
import base64
import docker


class PrimeRobotDefinitionFileMetadata(TypedDict):
    task_name: str
    description: str
    category: str
    message_init: str


class PrimeRobotDefinitionFile(TypedDict):
    metadata: PrimeRobotDefinitionFileMetadata
    container_name: str
    environments: Dict[str, Any]
    parameters: Dict[str, Any]


class PrimeRobotClient:

    token: str
    base_url = os.getenv(
        'APIGATEWAY_URL', 'https://5axnhjv2jc.execute-api.us-east-2.amazonaws.com/dev3')
    base_url_auth = os.getenv(
        'COGNITO_URL', 'https://prime-faturas-dev3.auth.us-east-2.amazoncognito.com')

    def __init__(self):
        self.token = self.__get_token__()

    def __get_token__(self):
        client_id = os.getenv('CLIENT_ID', '3dff3hdnqac9j9sli4b75o6b8p')
        client_secret = os.getenv(
            'CLIENT_SECRET', '1jfrc6n3g9opu92e8q36ca184brm9usufrs4v60ph7c96tb3mmlk')
        token = f'{client_id}:{client_secret}'.encode()
        base64bytes = base64.b64encode(token)
        token_base64 = base64bytes.decode()
        response = requests.post(  # type: ignore
            f'{self.base_url_auth}/oauth2/token',
            headers={
                'Authorization': f'Basic {token_base64}'
            },
            data={
                'grant_type': 'client_credentials'
            })
        return response.json()['access_token']  # type: ignore

    def register_task(self, task: PrimeRobotDefinitionFile):
        response = requests.post(  # type: ignore
            f'{self.base_url}/tasks/robots',
            headers={
                'Authorization': f'Bearer {self.token}'
            },
            json=task
        )
        result = json.loads(response.content)  # type: ignore
        print(result)
        if 'error' in result:
            raise Exception(result['erro'])

    def update_task(self, task: PrimeRobotDefinitionFile):
        response = requests.put(  # type: ignore
            f'{self.base_url}/tasks/robots',
            headers={
                'Authorization': f'Bearer {self.token}'
            },
            json=task
        )
        result = json.loads(response.content)  # type: ignore
        print(result)
        if 'error' in result:
            raise Exception(result['erro'])


class TaskRegister:

    def __get_primerobot_file_path__(self):
        return 'primerobot.yaml'

    def __get_primerobot_file__(self) -> str:
        with open(self.__get_primerobot_file_path__()) as primerobotfile:
            return primerobotfile.read()

    def __get_dockerfile_path__(self):
        return '.'

    def __execute_command__(self, command: str, *, cwd: str):
        process = subprocess.Popen(
            shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(output.strip().decode())
        rc = process.poll()
        return rc

    def get_account_id(self) -> str:
        return boto3.client('sts').get_caller_identity().get('Account')  # type: ignore # nopep8

    def get_region_name(self) -> str:
        session = boto3.session.Session()  # type: ignore
        return session.region_name  # type: ignore

    def register(self):
        try:
            print('Registrando robô...')
            is_new = True
            content = self.__get_primerobot_file__()

            content_dict: PrimeRobotDefinitionFile = yaml.load(
                content, Loader=yaml.FullLoader)

            repository_uri: str = content_dict.get('container_name')
            try:
                print('Criando registro do docker')
                ecr_client = boto3.client('ecr')
                response = ecr_client.create_repository(
                    repositoryName=content_dict['metadata']['task_name']
                )
                repository_uri: str = response['repository']['repositoryUri']
            except Exception as e:
                if 'RepositoryAlreadyExistsException' in str(e):
                    is_new = False
                    print('Registro do docker ja existe utilizando o mesmo')
                else:
                    print(str(e))

            print('Buildando imagem do docker')

            client = docker.APIClient()

            build_response = client.build(
                path=self.__get_dockerfile_path__(), tag=repository_uri, decode=True)
            for line in build_response:
                print(line.get('stream', '').replace('\n', ''))

            account_id = self.get_account_id()
            region_name = self.get_region_name()

            login_process = subprocess.Popen(
                shlex.split(
                    f'aws ecr get-login-password --region {region_name}'),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=self.__get_dockerfile_path__()
            )
            response = subprocess.check_output(
                shlex.split(
                    f'docker login --username AWS --password-stdin {account_id}.dkr.ecr.{region_name}.amazonaws.com'),
                stdin=login_process.stdout,
                cwd=self.__get_dockerfile_path__()
            )
            print(response.decode())
            login_process.wait()

            print('Enviando imagem para o repositorio')

            push_response = client.push(
                repository_uri,  decode=True, stream=True)
            for line in push_response:
                print(line)

            print('Imagem enviada para o repositorio')

            content_dict['container_name'] = repository_uri

            with open(self.__get_primerobot_file_path__(), 'w') as primerobotfile:
                yaml.dump(content_dict, primerobotfile)

            primerobot_client = PrimeRobotClient()
            if is_new:
                print('Adicionando robô a botplace')
                primerobot_client.register_task(content_dict)
            else:
                print('Atualizando robô na botplace')
                primerobot_client.update_task(content_dict)

        except Exception as e:
            traceback.print_exc()
            print(str(e))
