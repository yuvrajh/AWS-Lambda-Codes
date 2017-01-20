#!/usr/bin/env python
__author__ = 'surajsoma'

import boto3.ec2

def lambda_handler(event, context):

    # Insert Instance Ids to search 
    instance_ids = ['i-13231495','i-7c7b3bfa','i-0a06438c']
    volume_ids = []
    
    aws_regions = [
        'us-east-1',
        'us-west-1',
        'us-west-2',
        'ap-south-1',
        'ap-southeast-1',
        'ap-southeast-2',
        'ap-northeast-1',
        'eu-west-1',
        'sa-east-1'
    ]
    
    for rgn in aws_regions:
        print 'in region : ', rgn
        
        ec2 = boto3.client('ec2',region_name=rgn)
        response = response = ec2.describe_volumes(
            DryRun=False,
            
            Filters=[
                {
                    'Name': 'attachment.instance-id',
                    'Values': instance_ids
                }
            ]
        )
        
        print response['Volumes']
        
        
        for volume in response['Volumes']:
            for attachment in volume['Attachments']:
                print volume['VolumeId'], 'is attached to ', attachment['InstanceId'], ' SnapshotID : ', volume['SnapshotId']
                
            #print volume['VolumeId'], 'is attached to ', volume['Attachments']['InstanceId'] 
        
        
        
    return 'Volume Information Returned successfully'
