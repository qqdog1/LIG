import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    dynamodb.create_table(
        TableName='Boss_Info',
        KeySchema=[
            {
                'AttributeName': 'location_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'boss_id',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'location_id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'boss_id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return {
        'statusCode': 200
    }
