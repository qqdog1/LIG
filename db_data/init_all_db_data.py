import boto3
import os
import json

client = boto3.client('lambda')


def lambda_handler(event, context):
    lambda_function_name = [
        os.getenv('insert_location_data_function'),
        os.getenv('insert_level_info_data_function'),
        os.getenv('insert_equip_info_data_function'),
        os.getenv('insert_boss_info_data_function')
    ]

    for function_name in lambda_function_name:
        lambda_response_string = call_lambda(function_name)
        print(lambda_response_string)
        json_node = json.loads(lambda_response_string)
        if 'errorMessage' in json_node:
            print(function_name)

    return {
        'statusCode': 200
    }


def call_lambda(lambda_function_name):
    lambda_response = client.invoke(
        FunctionName=lambda_function_name,
        InvocationType='RequestResponse',
        Payload=''
    )
    return lambda_response['Payload'].read().decode("utf-8")
