import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    dynamodb.create_table(
        TableName='Location',
        KeySchema=[
            {
                'AttributeName': 'location_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'location_id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    return {
        'statusCode': 200
    }


