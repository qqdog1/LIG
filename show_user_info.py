import json
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    result = []
    line_uid = event['line_uid']
    table = dynamodb.Table('Player')
    db_result = table.get_item(Key={'line_uid': line_uid})

    if 'Item' in db_result.keys():
        item = db_result['Item']
        print(item)
        result.append('角色名稱: ' + item['name'] + ' 所在區域: ' + str(item['location_id']))
        result.append('等級: ' + str(item['lv']) + ' exp: ')
        result.append('持有金錢: ' + str(item['money']))
        result.append('生命: ' + ' 魔力: ')
        result.append('攻擊: ' + ' 防禦: ')
        result.append('速度: ')
    else:
        result.append('請先創建角色')

    json_dump = json.dumps(result, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')