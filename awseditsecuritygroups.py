import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
security_group_ids= ['sg-06c8ede2669dea5da', 'sg-0fe0844cb5a9f4ff6']

try:
    for i in security_group_ids:
    	data = ec2.authorize_security_group_ingress(
            GroupId=i,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                 ])
        print('Ingress Successfully Set %s' % data)

except ClientError as e:
    print(e)

