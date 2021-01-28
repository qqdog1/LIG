from linebot import (
    LineBotApi, WebhookHandler
)
import boto3
import logging
import os

from linebot.models import TextSendMessage

logger = logging.getLogger()
logger.setLevel(logging.INFO)

line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
client = boto3.client('lambda')


def lambda_handler(event, context):
    lambda_function_name = {
        'help': os.getenv('show_help_function'),
        'info': os.getenv('show_info_function')
    }[event['events'][0]['message']['text']]

    response = client.invoke(
        FunctionName=lambda_function_name,
        InvocationType='RequestResponse',
        Payload=''
    )

    response_string = response['Payload'].read().decode("utf-8")

    line_bot_api.reply_message(
        event['events'][0]['replyToken'],
        TextSendMessage(text=response_string))
    return {'statusCode': 200, 'body': 'OK'}
