import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

print(table.creation_date_time)

table.put_item(
    Item = {
     'username':'realchitresh',
     'firstname':'chitresh',
     'last_name':'notnice',
     'age':25,
     'accounttype':'standard_user',
    }
)

response = table.get_item(
    Key={
        'username':'realchitresh',
        'last_name':'notnice'
    }
)

item = response['Item']
print(item)