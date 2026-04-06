import boto3
import os
import json

# AWS clients
ses_client = boto3.client('ses')
sns_client = boto3.client('sns')

def send_email(event, context):
    body = json.loads(event['body'])
    response = ses_client.send_email(
        Source=os.environ['SES_EMAIL'],
        Destination={'ToAddresses': [body['to']]},
        Message={
            'Subject': {'Data': body['subject']},
            'Body': {'Text': {'Data': body['message']}}
        }
    )
    return {'statusCode': 200, 'body': json.dumps(response)}

def send_sms(event, context):
    body = json.loads(event['body'])
    response = sns_client.publish(
        PhoneNumber=body['to'],
        Message=body['message']
    )
    return {'statusCode': 200, 'body': json.dumps(response)}