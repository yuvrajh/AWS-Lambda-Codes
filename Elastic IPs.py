__author__ = 'VaibhavJain'

import boto3

def lambda_handler(event, context):
    
    # This will print all Elastic IPs that ate not allocated to any Ec2 instance.
    
    elastic_ips = []
    
    aws_regions = [
        "us-east-1",
        "us-west-1",
        "us-west-2",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-northeast-1",
        "eu-west-1",
        "sa-east-1"
    ]
    
    for reg in aws_regions:
        print "In Region : ", reg
        client = boto3.client('ec2',region_name=reg)
        response = client.describe_addresses()
        #print response
        #print response
        for address in response['Addresses']:
            if 'InstanceId' not in address:
                print address['PublicIp'], ' is not attched to any instance'
                
    return 'Elastic IPs Found'
