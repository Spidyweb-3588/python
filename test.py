
import boto3
import pandas as pd

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

AWS_REGION = 'us-east-1'
AWS_STORAGE_BUCKET_NAME = 'pysparkwrite'
FILE_NAME = 'part-00000-a4e2f798-ccce-4acd-9ad0-27197ac7b69a-c000.csv'

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

obj = s3.get_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=FILE_NAME)
df = pd.read_csv(obj)
print(df)