import json
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    result = []
    line_uid = event['line_uid']
    table = dynamodb.Table('Player')
    db_result = table.get_item(Key={'line_uid': line_uid})

    if 'Item' in db_result.keys():
        result = calc_and_reset(db_result['Item'])
    else:
        result.append('請先創建角色')

    json_dump = json.dumps(result, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')


def calc_and_reset(item):
    result = []
    if item['location_id'] != 0:
        result.append('')
    else:
        result.append('此區域無法獲得戰鬥經驗')
    return result
