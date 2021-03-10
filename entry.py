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
    is_pass_check = False
    line_uid = event['events'][0]['source']['userId']
    commands = event['events'][0]['message']['text'].split(' ')
    user_action = commands[0]

    lambda_function_name = get_lambda_function_name(user_action)
    if lambda_function_name == '':
        return {'statusCode': 200, 'body': 'OK'}

    data = {}
    if user_action == 'help':
        is_pass_check, data = prepare_help_data(line_uid)
    elif user_action == 'new':
        is_pass_check, data = prepare_new_user_data(line_uid, commands)
    elif user_action == 'info':
        is_pass_check, data = prepare_info_data(line_uid)
    elif user_action == 'map':
        is_pass_check, data = prepare_map_info_data(line_uid)
    elif user_action == 'move':
        is_pass_check, data = prepare_move_data(line_uid, commands)

    if is_pass_check:
        json_dump = json.dumps(data)
        response = call_lambda(lambda_function_name, json_dump)
    else:
        response = data

    line_bot_api.reply_message(
        event['events'][0]['replyToken'],
        TextSendMessage(text=response))
    return {'statusCode': 200, 'body': 'OK'}


def get_lambda_function_name(user_action):
    lambda_function_name = {
        'map': os.getenv('show_map_function'),
        'help': os.getenv('show_help_function'),
        'info': os.getenv('show_info_function'),
        'new': os.getenv('action_new_user_function'),
        'move': os.getenv('action_move_function')
    }

    if user_action in lambda_function_name:
        return lambda_function_name[user_action]
    return ''


def prepare_help_data(line_uid):
    data = {'line_uid': line_uid}
    return True, data


def prepare_new_user_data(line_uid, commands):
    if len(commands) >= 2 and commands[1] != '':
        data = {
            'line_uid': line_uid,
            'name': commands[1]
        }
        return True, data
    else:
        return False, '請輸入名稱'


def prepare_info_data(line_uid):
    data = {'line_uid': line_uid}
    return True, data


def prepare_map_info_data(line_uid):
    data = {'line_uid': line_uid}
    return True, data


def prepare_move_data(line_uid, commands):
    if len(commands) >= 2 and commands[1] != '':
        data = {
            'line_uid': line_uid,
            'location_id': commands[1]
        }
        return True, data
    else:
        return False, '請輸入要移動到的地方'


def call_lambda(lambda_function_name, data):
    lambda_response = client.invoke(
        FunctionName=lambda_function_name,
        InvocationType='RequestResponse',
        Payload=data
    )

    lambda_response_string = lambda_response['Payload'].read().decode("utf-8")

    json_node = json.loads(lambda_response_string)

    response = ''
    for command in json_node:
        response += command + '\n'
    return response
