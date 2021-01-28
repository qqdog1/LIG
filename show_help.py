import json


def lambda_handler(event, context):
    # check is user already create a character

    commands = ['info: 查看用戶資訊']
    json_dump = json.dumps(commands, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')
