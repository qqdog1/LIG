import json
import time

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


def calc_and_reset(player):
    result = []
    location_id = player['location_id']
    if location_id != 0:


        result.append('')
    else:
        result.append('此區域無法獲得戰鬥經驗')
    return result


def get_location_exp_and_money(location_id):
    table = dynamodb.Table('Location')
    db_result = table.get_item(Key={'location_id': location_id})

    if 'Item' in db_result.keys():
        location = db_result['Item']
        return location['exp'], location['money']
    else:
        print('找不到這個location id?' + location_id)
        return 0


def get_fight_count_and_new_update_time(last_update_time):
    current_time = int(time.time())
    diff = current_time - last_update_time
    fight_count = int(diff / 10)
    if fight_count > 2880:
        fight_count = 2880
    return fight_count, current_time


def get_exp_and_new_level(exp):
    pass


def update_player(lv, exp, money, update_time):
    pass
