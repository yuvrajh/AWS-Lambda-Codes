__author__ = 'surajso'

import boto3

def lambda_handler(event, context):
    
    exception_autoscaling_groups = []
    
    aws_regions = [
        "us-east-1",
        "us-west-1",
        "us-west-2",
        "ap-south-1",
        "ap-northeast-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-northeast-1",
        "eu-central-1",
        "eu-west-1",
        "sa-east-1"
    ]
    
    for rgn in aws_regions:
      print 'in region : ', rgn
      autoscaling = boto3.client('autoscaling')
    
      response = autoscaling.describe_auto_scaling_groups()
    
      ## Iterate reservations
      for group in response['AutoScalingGroups']:
        if group['DesiredCapacity'] > 0 and group['AutoScalingGroupName'] not in exception_autoscaling_groups:
            print 'Making Desired count of ', group['AutoScalingGroupName'], ' group to 0'
            response = autoscaling.set_desired_capacity(
                AutoScalingGroupName=group['AutoScalingGroupName'],
                DesiredCapacity=0,
                HonorCooldown=True
              )
    
    return 'Autoscalling Groups Stopped Succesfully'
