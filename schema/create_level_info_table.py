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
        BillingMode='PAY_PER_REQUEST'
    )

    return {
        'statusCode': 200
    }
