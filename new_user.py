import json
import boto3

dynamodb = boto3.resource('dynamodb')
player_table = dynamodb.Table('Player')


def lambda_handler(event, context):
    result = []
    line_uid = event['line_uid']
    name = event['name']

    if check_if_character_exist(line_uid):
        result.append('已創立過角色 創建新角色失敗')
    elif check_if_name_exist(name):
        result.append('角色名稱已被使用 請換個名稱')
    elif insert_new_name(line_uid, name):
        result.append('角色創建成功!!')
        result.append('輸入help查看可執行指令')
    else:
        print(event)
        result.append('角色創建失敗')

    json_dump = json.dumps(result, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')


def check_if_character_exist(line_uid):
    db_result = player_table.get_item(Key={'line_uid': line_uid})
    if 'Item' in db_result.keys():
        return True
    return False


def check_if_name_exist(name):
    response = player_table.scan(
        AttributesToGet=['name']
    )
    print(response)
    if response['Count'] > 0:
        for item in response['Items']:
            if item['name'] == name:
                return True
    return False


def insert_new_name(line_uid, name):
    put_result = player_table.put_item(Item={'line_uid': line_uid, 'name': name,
                                             'lv': 1, 'money': 0,
                                             'location_id': 0})
    if put_result['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    print(put_result)
    return False
