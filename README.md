# 🚀 AWS Serverless Messaging Service

A scalable serverless messaging system built using AWS services to send Email and SMS notifications.

---

## 📌 Features

- 📧 Send Emails using Amazon SES
- 📱 Send SMS using Amazon SNS
- ⚡ Serverless architecture using AWS Lambda
- 🌐 REST APIs via API Gateway
- 📬 Asynchronous messaging with Amazon SQS (in progress)

---

## 🏗️ Architecture

Client → API Gateway → Lambda → SES / SNS  
(Optional upgrade: API Gateway → SQS → Lambda → SES/SNS)

---

## 🛠️ Tech Stack

- AWS Lambda
- Amazon API Gateway
- Amazon SES (Email)
- Amazon SNS (SMS)
- Amazon SQS (Queue)
- Python (Boto3)
- Serverless Framework

---

## 🚀 API Endpoints

### Send Email

POST /dev/email

```json
{
  "to": "example@gmail.com",
  "subject": "Test Email",
  "message": "Hello from AWS Lambda"
}
