import json
import boto3

dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    result = []
    line_uid = event['line_uid']
    name = event['name']
    db_result = dynamodb.get_item(TableName='Player', Key={'line_uid': {'S': line_uid}})

    if 'Item' in db_result.keys():
        result.append('已創立過角色 創建新角色失敗')
    else:
        put_result = dynamodb.put_item(TableName='Player', Item={'line_uid':{'S':line_uid},'name':{'S':name}})
        print(put_result)
        result.append('角色創建成功!!')
        result.append('輸入help查看可執行指令')

    json_dump = json.dumps(result, ensure_ascii=False)

    return bytes(json_dump, 'utf-8')
