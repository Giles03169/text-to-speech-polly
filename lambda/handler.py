---

## 🐍 `lambda_function.py`

```python
import json
import boto3
import uuid

polly = boto3.client('polly')
s3 = boto3.client('s3')

BUCKET_NAME = 'polly-audio-output-giles'

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))

        body = json.loads(event['body'])
        text = body.get('text', 'Hello from Polly!')
        voice_id = body.get('voiceId', 'Joanna')  # Default voice

        # Call Polly to synthesize speech
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_id
        )

        audio_stream = response['AudioStream'].read()
        filename = f"{uuid.uuid4()}.mp3"

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=audio_stream,
            ContentType='audio/mpeg'
        )

        # Public URL
        audio_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps({'audioUrl': audio_url})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
