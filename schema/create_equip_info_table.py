import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    dynamodb.create_table(
        TableName='Equip_Info',
        KeySchema=[
            {
                'AttributeName': 'part_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'equip_id',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'part_id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'equip_id',
                'AttributeType': 'N'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )

    return {
        'statusCode': 200
    }
