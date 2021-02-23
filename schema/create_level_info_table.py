import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    dynamodb.create_table(
        TableName='Level_Info',
        KeySchema=[
            {
                'AttributeName': 'lv',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'lv',
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
