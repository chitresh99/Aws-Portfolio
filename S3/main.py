import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
with open('aws.jpg', 'rb') as data:
    s3.Bucket('newtryingbucket').put_object(Key='aws.jpg', Body=data)