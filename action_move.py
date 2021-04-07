import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
client = boto3.client('lambda')
player_table = dynamodb.Table('Player')


def lambda_handler(event, context):
    result = []
    line_uid = event['line_uid']
    location_id = int(event['location_id'])

    is_user_exist, is_pass = is_pass_location(line_uid, location_id)
    if is_user_exist:
        if is_pass:
            response = move_to_location(line_uid, location_id)
            result.append('前次地圖戰鬥結果')
            json_node = json.loads(response)
            for msg in json_node:
                result.append(msg)
            result.append(' ')
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
    db_result = player_table.get_item(Key={'line_uid': line_uid})
    location_number = get_location_number(location_id)

    if 'Item' in db_result.keys():
        player = db_result['Item']
        passed_location = player['passed_location']
        if location_number == (int(passed_location) & location_number):
            return True, True
        return True, False
    else:
        return False, False


def get_location_number(location_id):
    if location_id > 2:
        return pow(2, location_id - 1)
    return location_id


def move_to_location(line_uid, location_id):
    response = call_check_lambda_function(line_uid)
    print(response)
    update_player(line_uid, location_id)
    return response


def call_check_lambda_function(line_uid):
    data = {'line_uid': line_uid}
    json_dump = json.dumps(data)
    lambda_response = client.invoke(
        FunctionName=os.getenv('action_check_function'),
        InvocationType='RequestResponse',
        Payload=json_dump
    )

    return lambda_response['Payload'].read().decode("utf-8")


def update_player(line_uid, location_id):
    response = player_table.update_item(
        Key={'line_uid': line_uid},
        UpdateExpression='set location_id=:location_id',
        ExpressionAttributeValues={':location_id': location_id},
        ReturnValues="UPDATED_NEW"
    )
    print(response)
