#!/usr/bin/env python
__author__ = 'surajsoma'

import boto3.ec2

def lambda_handler(event, context):

    running_instance_ids = []
    exception_instance_ids = []
    
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
        response = ec2.describe_instances(
            DryRun=False,
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': ['running']
                }
            ]
        )
        
        ## Iterate reservations
        #print response
        for reservation in response['Reservations']:
            for inst in reservation['Instances']:
                running_instance_ids.append(inst['InstanceId'])
    
        print "running instance ids : ", running_instance_ids
        print "exception instance ids : ", exception_instance_ids
        instance_ids_to_be_stopped = list(set(running_instance_ids) - set(exception_instance_ids))
        print "instance_ids_to_be_stopped : ", instance_ids_to_be_stopped
        running_instance_ids = []
        if len(instance_ids_to_be_stopped) > 0:
            response = ec2.stop_instances(
                DryRun=False,
                InstanceIds=instance_ids_to_be_stopped,
                Force=True
            )
        
    return 'Instances Stopped Succesfully'
