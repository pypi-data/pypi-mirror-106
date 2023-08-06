import os
from typing import Any, Optional
import yaml
import pandas as pd
import boto3
from datetime import datetime
from gql import gql, Client, AIOHTTPTransport


class GraphQLClient:

    def __init__(self):
        transport = AIOHTTPTransport(
            url=os.environ.get(
                'GRAPHQL_URL', 'https://mqj2oaop3fdcplw5ev3vxsqewi.appsync-api.us-east-2.amazonaws.com/graphql'),
            headers={
                'X-Api-Key': os.environ.get('GRAPHQL_API_KEY', 'da2-7ym5pekywrbrrotak7hvlqq4vi')}
        )
        self.client = Client(
            transport=transport,
            fetch_schema_from_transport=True)

    def atualizar_task_progress(self,
                                id: str,
                                description: Optional[str] = None,
                                total: Optional[int] = None,
                                actual: Optional[int] = None,
                                completed: Optional[bool] = None,
                                error: Optional[str] = None,
                                success: Optional[str] = None,
                                stop: Optional[bool] = None) -> None:
        mutation = gql("""
            mutation updateTaskProgress($input: UpdateTaskProgressInput!) {
                updateTaskProgress(input: $input) {
                    id
                    description
                    total
                    actual
                    completed
                    custom_name
                    error
                    success
                    start_date
                    end_date
                    stop
                }
            }
        """)

        data = {
            'id': id,
            'description': description,
            'total': total,
            'actual': actual,
            'completed': completed,
            'error': error,
            'success': success,
            'stop': stop
        }
        copy_data = data.copy()
        for key in copy_data.keys():
            if data[key] is None:
                del data[key]

        if error or success:
            data['end_date'] = self.get_date_now_dynamo()
            data['completed'] = True
        else:
            print(data.get('description'))

        self.client.execute(mutation, variable_values={'input': data})

    def get_date_now_dynamo(self) -> str:
        dynamo_date_format = '%Y-%m-%dT%H:%M:%SZ'
        start_date = datetime.now()
        start_date_string = start_date.strftime(dynamo_date_format)
        return start_date_string


class TaskProgressRepositorio:

    table: Any

    def __init__(self):
        dynamodb_client = boto3.resource('dynamodb')
        self.table = dynamodb_client.Table(
            os.getenv('DB_TASK_PROGRESS', 'task_progress_dev3'))

    def obter_por_id(self, task_id):
        response = self.table.get_item(
            Key={'id': task_id}
        )
        return response.get('Item')


class PrimeRobot:

    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    task_id: Optional[str] = os.getenv('TASK_ID')
    task_progress_repositorio: TaskProgressRepositorio
    task_progress: GraphQLClient
    first_error = ''

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        if self.is_aws():
            self.task_progress_repositorio = TaskProgressRepositorio()
            self.task_progress = GraphQLClient()

    def _start_test(self, name, attrs):
        if self.is_aws():
            self.task_progress.atualizar_task_progress(
                id=self.task_id,
                description=name
            )

    def _end_test(self, name, attrs):
        if 'FAIL' in attrs['status'] and not self.first_error:
            self.first_error = attrs['message']

    def _end_suite(self, name, attrs):
        if self.is_aws():
            if attrs['status'] == 'PASS':
                self.task_progress.atualizar_task_progress(
                    id=self.task_id,
                    success='Task finalizada com sucesso!!!'
                )
            else:
                self.task_progress.atualizar_task_progress(
                    id=self.task_id,
                    error=self.first_error
                )

    def _obter_primerobot_content(self):
        with open("primerobot.yaml") as primerobotfile:
            content = primerobotfile.read()
            return yaml.load(content, Loader=yaml.FullLoader)

    def is_aws(self):
        return self.task_id is not None

    def obter_parametros(self):
        parameters_values = {}
        if self.is_aws():
            task_progress = self.task_progress_repositorio.obter_por_id(
                self.task_id)
            parameters_values = task_progress['parameters']
        else:
            primerobot_dict = self._obter_primerobot_content()

            parameters_values = {}
            for parameter in primerobot_dict['parameters']:
                if not parameters_values.get(parameter):
                    if primerobot_dict['parameters'][parameter]['type'] == 'array':
                        parameters_values[parameter] = []

                file_data = primerobot_dict['parameters'][parameter].get(
                    'data')
                if file_data:
                    if '.xlsx' in file_data:
                        dataframe = pd.read_excel(file_data)
                        for item, key in dataframe.iterrows():
                            value = str(key[parameter])
                            parameters_values[parameter].append(value)
                    else:
                        print('Arquivo não implementado como input')

        return parameters_values

    def salvar_output(self, dataframe):
        primerobot_dict = self._obter_primerobot_content()
        output = primerobot_dict.get('output')
        if output:
            dataframe.to_excel(output['data'], index=False)

        if self.is_aws():
            s3_client = boto3.client('s3')
            s3_client.upload_file(
                '/app/output/output.xml', os.environ['BUCKET_RESULTADOS'], f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/output.xml')
            s3_client.upload_file(
                '/app/output/log.html', os.environ['BUCKET_RESULTADOS'], f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/log.html')
            if output:
                s3_client.upload_file(output['data'], os.environ['BUCKET_RESULTADOS'],
                                      f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/{output["data"]}')
