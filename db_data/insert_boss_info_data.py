import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Boss_Info')


def lambda_handler(event, context):
    data = {0: [{'boss_id': 1, 'name': '大牛', 'hp': 250, 'at': 5, 'def': 1, 'spd': 8}],
            1: [{'boss_id': 1, 'name': '老虎', 'hp': 500, 'at': 10, 'def': 1, 'spd': 11}],
            2: [{'boss_id': 1, 'name': 'XX怪', 'hp': 2000, 'at': 25, 'def': 1, 'spd': 10}],
            3: [{'boss_id': 1, 'name': 'AA王', 'hp': 5000, 'at': 30, 'def': 1, 'spd': 10}],
            4: [{'boss_id': 1, 'name': 'XX壞蛋', 'hp': 10000, 'at': 40, 'def': 1, 'spd': 10}],
            5: [{'boss_id': 1, 'name': '圈圈魔頭', 'hp': 20000, 'at': 55, 'def': 1, 'spd': 7}],
            6: [{'boss_id': 1, 'name': '墮落的誰誰誰', 'hp': 50000, 'at': 88, 'def': 1, 'spd': 9}],
            7: [{'boss_id': 1, 'name': '怎樣的啥東西', 'hp': 100000, 'at': 120, 'def': 1, 'spd': 11}],
            8: [{'boss_id': 1, 'name': '誰前面的使者', 'hp': 150000, 'at': 250, 'def': 1, 'spd': 10}],
            9: [{'boss_id': 1, 'name': '某某某', 'hp': 999999, 'at': 999, 'def': 99, 'spd': 10}],}

    for location_id in data:
        location = data[location_id]
        for var in location:
            put_result = table.put_item(Item={'location_id': location_id, 'boss_id': var['boss_id'],
                                              'name': var['name'], 'hp': var['hp'], 'at': var['at'],
                                              'def': var['def'], 'spd': var['spd']})
            if put_result['ResponseMetadata']['HTTPStatusCode'] != 200:
                print(put_result)

    return {
        'statusCode': 200
    }
