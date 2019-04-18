import boto3
import json
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['sg-06c8ede2669dea5da'])
    print (json.dumps(response, sort_keys=True))
except ClientError as e:
    print(e)
