import json
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    result = []
    line_uid = event['line_uid']
    location_id = event['location_id']

    is_user_exist, is_pass = is_pass_location(line_uid, location_id)
    if is_user_exist:
        if is_pass:
            move_to_location(line_uid, location_id)
            result.append('已移動至該區域')
        else:
            result.append('需先打敗區域守衛')
            result.append('輸入fight ' + str(location_id))
            result.append('挑戰區域守衛')
    else:
        result.append('請先創建角色')

    json_dump = json.dumps(result, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')


def is_pass_location(line_uid, location_id):
    table = dynamodb.Table('Player')
    db_result = table.get_item(Key={'line_uid': line_uid})
    location_number = get_location_number(location_id)

    if 'Item' in db_result.keys():
        player = db_result['Item']
        passed_location = player['pass_location']
        if location_number == (passed_location & location_number):
            return True, True
        return True, False
    else:
        return False, False


def get_location_number(location_id):
    if location_id > 2:
        return pow(2, location_id - 1)
    return location_id


def move_to_location(line_uid, location_id):
    # call check function
    # update user location
    pass
