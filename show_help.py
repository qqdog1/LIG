import json
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    commands = ['支援的指令:']
    line_uid = event['line_uid']
    table = dynamodb.Table('Player')
    db_result = table.get_item(Key={'line_uid': line_uid})

    if 'Item' in db_result.keys():
        commands.append('info: 查看角色資訊')
        commands.append('map: 查看地圖資訊')
        commands.append('item: 查看道具')
        commands.append('city: 查看個人城市')
    else:
        commands.append('new 角色名稱: 輸入new 空格 角色名稱以創建新角色!!')

    json_dump = json.dumps(commands, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')
