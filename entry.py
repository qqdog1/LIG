from linebot import (
    LineBotApi, WebhookHandler
)
import boto3
import os
import json

from linebot.models import TextSendMessage

line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
client = boto3.client('lambda')


def lambda_handler(event, context):
    lambda_function_name = {
        'help': os.getenv('show_help_function'),
        'info': os.getenv('show_info_function'),
        'new': os.getenv('create_user_function')
    }[event['events'][0]['message']['text']]

    user_id = event['events'][0]['source']['userId']
    data = {'line_uid': user_id}
    json_dump = json.dumps(data)

    lambda_response = client.invoke(
        FunctionName=lambda_function_name,
        InvocationType='RequestResponse',
        Payload=json_dump
    )

    lambda_response_string = lambda_response['Payload'].read().decode("utf-8")

    json_node = json.loads(lambda_response_string)

    response = ''
    for command in json_node:
        response += command + '\n'

    line_bot_api.reply_message(
        event['events'][0]['replyToken'],
        TextSendMessage(text=response))
    return {'statusCode': 200, 'body': 'OK'}
