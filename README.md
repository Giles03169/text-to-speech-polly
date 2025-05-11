# 🗣️ AWS Serverless Text-to-Speech App

This project converts text into speech using Amazon Polly, triggered via API Gateway and AWS Lambda. The resulting audio file is saved to Amazon S3 and returned as a public URL.

## 🚀 Stack
- AWS Lambda (Python)
- Amazon Polly
- Amazon S3 (for public MP3 access)
- API Gateway (HTTP API)

---

## 📦 Functionality

1. The frontend or API client (e.g. Postman) sends a `POST` request to API Gateway.
2. The Lambda function:
   - Takes text input
   - Synthesizes speech using Amazon Polly
   - Uploads the MP3 to a public S3 bucket
   - Returns a public audio URL in the response

---

## 🧪 Sample Input

**POST** (https://zi3whs7mk5.execute-api.eu-west-1.amazonaws.com/dev/speak)

```json
{
  "text": "Hello from Giles, This is Polly working.",
  "voiceId": "Joanna"
}
