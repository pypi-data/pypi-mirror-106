import os
from typing import Any
import yaml
import pandas as pd
import boto3
from datetime import datetime


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

    def finalizar_task(self, task_id: str):
        self.table.update_item(
            Key={
                'id': task_id
            },
            UpdateExpression='set completed = :completed, end_date = :end_date',
            ExpressionAttributeValues={
                ':completed': True,
                ':end_date': self.get_date_now_dynamo()
            },
        )

    def get_date_now_dynamo(self) -> str:
        dynamo_date_format = '%Y-%m-%dT%H:%M:%SZ'
        start_date = datetime.now()
        start_date_string = start_date.strftime(dynamo_date_format)
        return start_date_string


def obter_primerobot_content():
    with open("primerobot.yaml") as primerobotfile:
        content = primerobotfile.read()
        return yaml.load(content, Loader=yaml.FullLoader)


def is_aws():
    return os.getenv('TASK_ID') is not None


def obter_parametros():
    parameters_values = {}
    if is_aws():
        task_progress_repositorio = TaskProgressRepositorio()

        task_progress = task_progress_repositorio.obter_por_id(
            os.getenv('TASK_ID'))
        parameters_values = task_progress['parameters']
    else:
        primerobot_dict = obter_primerobot_content()

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


def salvar_output(dataframe):
    primerobot_dict = obter_primerobot_content()
    output = primerobot_dict.get('output')
    if output:
        dataframe.to_excel(output['data'], index=False)

    if is_aws():
        s3_client = boto3.client('s3')
        s3_client.upload_file(
            '/app/output/output.xml', os.environ['BUCKET_RESULTADOS'], f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/output.xml')
        s3_client.upload_file(
            '/app/output/log.html', os.environ['BUCKET_RESULTADOS'], f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/log.html')
        if output:
            s3_client.upload_file(output['data'], os.environ['BUCKET_RESULTADOS'],
                                  f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/{output["data"]}')
        finalizar_task()


def finalizar_task():
    task_progress_repositorio = TaskProgressRepositorio()
    task_progress_repositorio.finalizar_task(os.getenv('TASK_ID'))
