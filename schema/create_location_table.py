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
        BillingMode='PAY_PER_REQUEST'
    )

    return {
        'statusCode': 200
    }


