import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Location')


def lambda_handler(event, context):
    data = {0: {'name': '什麼偏遠鄉村的', 'exp': 3, 'money': 1},
            1: {'name': 'XX小徑', 'exp': 10, 'money': 3},
            2: {'name': 'XX森林', 'exp': 35, 'money': 5},
            3: {'name': 'XX洞穴', 'exp': 100, 'money': 10},
            4: {'name': '淪陷XX城', 'exp': 350, 'money': 18},
            5: {'name': 'XX道路', 'exp': 1000, 'money': 25},
            6: {'name': 'XX山脈', 'exp': 3500, 'money': 40},
            7: {'name': 'XX遺跡', 'exp': 10000, 'money': 100},
            8: {'name': 'XX城堡', 'exp': 35000, 'money': 250},
            9: {'name': 'XX大廳', 'exp': 100000, 'money': 999}}

    for location_id in data:
        location_data = data[location_id]
        put_result = table.put_item(Item={'location_id': location_id,
                                          'name': location_data['name'],
                                          'exp': location_data['exp'],
                                          'money': location_data['money']})
        if put_result['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(put_result)

    return {
        'statusCode': 200
    }
