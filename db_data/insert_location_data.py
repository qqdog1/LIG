import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Location')


def lambda_handler(event, context):
    data = {0: '什麼偏遠鄉村的',
            1: 'XX小徑',
            2: 'XX森林',
            3: 'XX洞穴',
            4: '淪陷XX城',
            5: 'XX道路',
            6: 'XX山脈',
            7: 'XX遺跡',
            8: 'XX城堡',
            9: 'XX大廳'}

    for location_id in data:
        put_result = table.put_item(Item={'location_id': location_id, 'name': data[location_id]})
        if put_result['ResponseMetadata']['HTTPStatusCode'] != 200:
            print(put_result)

    return {
        'statusCode': 200
    }
