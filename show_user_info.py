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
        level_info = getLevelInfo(item['lv'])
        result.append('角色名稱: ' + item['name'] + ' 所在區域: ' + getLocationName(item['location_id']))
        result.append('等級: ' + str(item['lv']) + ' exp: ' + str(item['exp']) + "/" + str(level_info['lv']))
        result.append('持有金錢: ' + str(item['money']))
        result.append('生命: ' + str(level_info['hp']) + ' 魔力: ' + str(level_info['mp']))
        result.append('攻擊: ' + str(level_info['at']) + ' 防禦: ' + str(level_info['def']))
        result.append('速度: ' + str(level_info['spd']))
    else:
        result.append('請先創建角色')

    json_dump = json.dumps(result, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')


def getLocationName(location_id):
    table = dynamodb.Table('Location')
    db_result = table.get_item(Key={'location_id': location_id})
    if 'Item' in db_result.keys():
        item = db_result['Item']
        return item['name']
    else:
        print('找不到對應的location id:' + location_id)
        return '???'


def getLevelInfo(lv):
    table = dynamodb.Table('Level_Info')
    db_result = table.get_item(Key={'lv': lv})
    if 'Item' in db_result.keys():
        item = db_result['Item']
        return item
    else:
        print('找不到對應的等級資訊:' + lv)
        return '???'
