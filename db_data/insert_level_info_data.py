import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Level_Info')


def lambda_handler(event, context):
    data = {1: {'exp': 10, 'hp': 10, 'mp': 5, 'at': 3, 'def': 0, 'spd': 10},
            2: {'exp': 20, 'hp': 15, 'mp': 8, 'at': 5, 'def': 1, 'spd': 10},
            3: {'exp': 50, 'hp': 22, 'mp': 11, 'at': 8, 'def': 1, 'spd': 10},
            4: {'exp': 120, 'hp': 34, 'mp': 16, 'at': 12, 'def': 2, 'spd': 11},
            5: {'exp': 250, 'hp': 50, 'mp': 23, 'at': 18, 'def': 2, 'spd': 11},
            6: {'exp': 600, 'hp': 73, 'mp': 29, 'at': 25, 'def': 2, 'spd': 11},
            7: {'exp': 1300, 'hp': 102, 'mp': 36, 'at': 33, 'def': 3, 'spd': 11},
            8: {'exp': 2700, 'hp': 144, 'mp': 45, 'at': 40, 'def': 3, 'spd': 11},
            9: {'exp': 5500, 'hp': 201, 'mp': 58, 'at': 47, 'def': 4, 'spd': 11},
            10: {'exp': -1, 'hp': 278, 'mp': 67, 'at': 55, 'def': 5, 'spd': 12}}

    for lv in data:
        var = data[lv]
        put_result = table.put_item(Item={'lv': lv, 'exp': var['exp'], 'hp': var['hp'], 'mp': var['mp'],
                                          'at': var['at'], 'def': var['def'], 'spd': var['spd']})
        if put_result['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(put_result)

    return {
        'statusCode': 200
    }
