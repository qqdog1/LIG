import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('location')


def lambda_handler(event, context):


    return {
        'statusCode': 200
    }


