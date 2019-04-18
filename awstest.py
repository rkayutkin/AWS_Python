import boto3
import json

ec2 = boto3.client('ec2')
security_group = ec2.SecurityGroup('sg-06c8ede2669dea5da')

response = security_group.authorize_ingress(
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'Added Via Python Script'
                },
            ]
        },
    ],
)
