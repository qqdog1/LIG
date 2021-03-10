import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Location')


def lambda_handler(event, context):
    data = {0: {'name': '什麼偏遠鄉村的', 'exp': 3},
            1: {'name': 'XX小徑', 'exp': 10},
            2: {'name': 'XX森林', 'exp': 35},
            3: {'name': 'XX洞穴', 'exp': 100},
            4: {'name': '淪陷XX城', 'exp': 350},
            5: {'name': 'XX道路', 'exp': 1000},
            6: {'name': 'XX山脈', 'exp': 3500},
            7: {'name': 'XX遺跡', 'exp': 10000},
            8: {'name': 'XX城堡', 'exp': 35000},
            9: {'name': 'XX大廳', 'exp': 100000}}

    for location_id in data:
        location_data = data[location_id]
        put_result = table.put_item(Item={'location_id': location_id,
                                          'name': location_data['name'],
                                          'exp': location_data['exp']})
        if put_result['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(put_result)

    return {
        'statusCode': 200
    }
