import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    dynamodb.create_table(
        TableName='Player',
        KeySchema=[
            {
                'AttributeName': 'line_uid',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'line_uid',
                'AttributeType': 'S'
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


