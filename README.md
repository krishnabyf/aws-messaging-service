# AWS Serverless Messaging Service

Scalable serverless messaging backend for sending email and SMS notifications through AWS-managed services. This repository is structured as a practical AWS backend portfolio project with Lambda, API Gateway, SES, SNS, and Serverless Framework deployment configuration.

## Features

- Send emails with Amazon SES.
- Send SMS messages with Amazon SNS.
- Serverless REST API through API Gateway and AWS Lambda.
- Queue-ready architecture for asynchronous SQS-based processing.
- Python handler code with a simple local syntax validation path.

## Architecture

Client -> API Gateway -> Lambda -> SES / SNS

Optional production extension:

Client -> API Gateway -> SQS -> Lambda -> SES / SNS

## Tech Stack

- AWS Lambda
- Amazon API Gateway
- Amazon SES
- Amazon SNS
- Amazon SQS
- Python and Boto3
- Serverless Framework

## Project Structure

aws-messaging/
  README.md
  messaging-service/
    handler.py
    requirements.txt
    serverless.yml

## API Examples

Send email:

POST /dev/email

Request body:

  {
    "to": "example@gmail.com",
    "subject": "Test Email",
    "message": "Hello from AWS Lambda"
  }

Send SMS:

POST /dev/sms

Request body:

  {
    "phone": "+15555550123",
    "message": "Deployment notification"
  }

## Local Validation

cd messaging-service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m py_compile handler.py

## Deploy

cd messaging-service
serverless deploy

## Production Improvements

- Add SQS dead-letter queues.
- Add CloudWatch alarms for Lambda failures and throttles.
- Add request validation and API authentication.
- Add integration tests with mocked AWS clients.

## Author

Krishna Mankali
