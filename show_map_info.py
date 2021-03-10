import json
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    result = []
    line_uid = event['line_uid']

    is_create_user, location_id = get_user_location(line_uid)

    if is_create_user:
        item = get_location_info()
        sorted_item = sorted(item, key=lambda s: s['location_id'])
        for location in sorted_item:
            if location['location_id'] == location_id:
                result.append(str(location['location_id']) + ": " + location['name'] + "(現在位置)")
            else:
                result.append(str(location['location_id']) + ": " + location['name'])
    else:
        result.append('請先創建角色')

    json_dump = json.dumps(result, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')


def get_user_location(line_uid):
    table = dynamodb.Table('Player')
    db_result = table.get_item(Key={'line_uid': line_uid})

    if 'Item' in db_result.keys():
        player = db_result['Item']
        return True, player['location_id']
    else:
        return False, 0


def get_location_info():
    table = dynamodb.Table('Location')
    db_result = table.scan()
    if 'Items' in db_result.keys():
        return db_result['Items']
    else:
        print('location資料不存在?')
        return ''
