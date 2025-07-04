import json
import boto3
import datetime
import uuid
import os

# Get table name from environment variable
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',  # ✅ Allow requests from any origin
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    }

    # ✅ Handle preflight (OPTIONS) requests
    if event['requestContext']['http']['method'] == "OPTIONS":
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'CORS preflight success'})
        }

    try:
        body = json.loads(event['body'])

        name = body.get('name')
        email = body.get('email')
        message = body.get('message')
        timestamp = datetime.datetime.utcnow().isoformat()

        if not (name and email and message):
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'success': False, 'message': 'Missing fields'})
            }

        form_id = str(uuid.uuid4())  # Unique ID for each submission

        table.put_item(
            Item={
                'id': form_id,
                'name': name,
                'email': email,
                'message': message,
                'timestamp': timestamp
            }
        )

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'success': True, 'message': 'Data stored successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'success': False, 'message': str(e)})
        }
