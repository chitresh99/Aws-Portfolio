import boto3
s3 = boto3.client('s3')
file_path = r'\Redshift\category_pipe.txt'
s3.upload_file(file_path, 'datatoupload', 'category_pipe.txt')
