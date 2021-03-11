import json
import time
import boto3

dynamodb = boto3.resource('dynamodb')
player_table = dynamodb.Table('Player')


def lambda_handler(event, context):
    result = []
    line_uid = event['line_uid']
    db_result = player_table.get_item(Key={'line_uid': line_uid})

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
        location_exp, location_money = get_location_exp_and_money(location_id)
        fight_count, new_update_time = get_fight_count_and_new_update_time(player['last_update_time'])
        gain_exp = location_exp * fight_count
        gain_money = location_money * fight_count
        new_money = gain_money + player['money']
        new_exp, new_lv = get_exp_and_new_level(gain_exp, player['exp'], player['lv'])
        update_player(player['line_uid'], new_lv, new_exp, new_money, new_update_time)

        result.append('經歷 ' + str(fight_count) + '次戰鬥')
        result.append('獲得 ' + str(gain_exp) + '經驗 ' + str(gain_money) + '金錢')
        if new_lv > player['lv']:
            result.append('等級提升到 ' + str(new_lv))
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
        print('找不到這個location id?' + str(location_id))
        return 0, 0


def get_fight_count_and_new_update_time(last_update_time):
    current_time = int(time.time())
    diff = current_time - last_update_time
    fight_count = int(diff / 10)
    if fight_count > 2880:
        fight_count = 2880
    return fight_count, current_time


def get_exp_and_new_level(gain_exp, player_exp, player_lv):
    level_info = {}
    exp = gain_exp + player_exp

    table = dynamodb.Table('Level_Info')
    db_result = table.scan()
    if 'Items' in db_result.keys():
        items = db_result['Items']
        for item in items:
            level_info[item['lv']] = item
    else:
        print('location資料不存在?')
        return exp, player_lv

    while True:
        if player_lv in level_info.keys():
            lv_exp = level_info[player_lv]['exp']
            if exp >= lv_exp:
                player_lv = player_lv + 1
                exp = exp - lv_exp
            else:
                break
        else:
            break

    return exp, player_lv


def update_player(line_uid, lv, exp, money, update_time):
    response = player_table.update_item(
        Key={'line_uid': line_uid},
        UpdateExpression='set lv=:lv, exp=:exp, money=:money, last_update_time=:last_update_time',
        ExpressionAttributeValues={':lv': lv, ':exp': exp, ':money': money, ':last_update_time': update_time},
        ReturnValues="UPDATED_NEW"
    )
    print(response)
