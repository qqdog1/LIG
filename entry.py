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
    call_lambda = True
    response = ''
    error_msg = ''
    line_uid = event['events'][0]['source']['userId']
    commands = event['events'][0]['message']['text'].split(' ')
    user_action = commands[0]

    lambda_function_name = {
        'help': os.getenv('show_help_function'),
        'info': os.getenv('show_info_function'),
        'new': os.getenv('create_user_function')
    }[user_action]

    data = {}
    if user_action == 'help':
        data = prepare_help_data(line_uid)
    elif user_action == 'new':
        if len(commands) >= 2 and commands[1] != '':
            data = prepare_new_user_data(line_uid, commands[1])
        else:
            call_lambda = False
            error_msg = '請輸入名稱'

    if call_lambda:
        json_dump = json.dumps(data)

        lambda_response = client.invoke(
            FunctionName=lambda_function_name,
            InvocationType='RequestResponse',
            Payload=json_dump
        )

        lambda_response_string = lambda_response['Payload'].read().decode("utf-8")

        json_node = json.loads(lambda_response_string)

        for command in json_node:
            response += command + '\n'
    else:
        response = error_msg

    line_bot_api.reply_message(
        event['events'][0]['replyToken'],
        TextSendMessage(text=response))
    return {'statusCode': 200, 'body': 'OK'}


def prepare_help_data(line_uid):
    data = {'line_uid': line_uid}
    return data


def prepare_new_user_data(line_uid, name):
    data = {
        'line_uid': line_uid,
        'name': name
    }
    return data
