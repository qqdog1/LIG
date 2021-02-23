import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Equip_Info')


def lambda_handler(event, context):
    data = {1: [{'equip_id': 1, 'name': 'XX帽', 'hp': 1, 'mp': 0, 'at': 0, 'def': 1, 'spd': 0},
                {'equip_id': 2, 'name': 'XX頭盔', 'hp': 0, 'mp': 0, 'at': 0, 'def': 2, 'spd': 0}],
            2: [{'equip_id': 1, 'name': 'XX衣', 'hp': 0, 'mp': 0, 'at': 0, 'def': 3, 'spd': 0},
                {'equip_id': 2, 'name': 'XX盔甲', 'hp': 0, 'mp': 0, 'at': 0, 'def': 4, 'spd': 0}],
            3: [{'equip_id': 1, 'name': 'XX鞋', 'hp': 0, 'mp': 0, 'at': 0, 'def': 0, 'spd': 1},
                {'equip_id': 2, 'name': '跑鞋', 'hp': 0, 'mp': 0, 'at': 0, 'def': 1, 'spd': 1}],
            4: [{'equip_id': 1, 'name': '叉子', 'hp': 0, 'mp': 2, 'at': 0, 'def': 0, 'spd': 0},
                {'equip_id': 2, 'name': '刀', 'hp': 0, 'mp': 0, 'at': 2, 'def': 0, 'spd': 0}]}

    for part_id in data:
        part = data[part_id]
        for var in part:
            put_result = table.put_item(Item={'part_id': part_id, 'equip_id': var['equip_id'], 'hp': var['hp'],
                                              'mp': var['mp'], 'at': var['at'], 'def': var['def'], 'spd': var['spd'],
                                              'name': var['name']})
            if put_result['ResponseMetadata']['HTTPStatusCode'] != 200:
                print(put_result)

    return {
        'statusCode': 200
    }
