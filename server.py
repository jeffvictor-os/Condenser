""" Condenser: a demonstration of automated creation of EC2 instances (AWS VMs) using
    the AWS Python API boto3. This could be extended to shorten the elapsed time of
    a compute-itensive workload by breaking it into chunks, each chunk computed by 
    one of the VMs.
    There are better ways to do this; this project is just a demonstration.
"""
import yaml

import boto3

# Read AWS configuration information.
with open('../config.yaml') as cfgfile:
    config = yaml.safe_load(cfgfile)

# Read boot script into DROP_BOOT_SCRIPT
with open('user_data') as boot_file:
    DROP_BOOT_SCRIPT = boot_file.read()

ec2_rsrc = boto3.resource('ec2')

# Create these in a loop so they can each have a name.
for i in range(config['drop_qty']):
    drop = ec2_rsrc.create_instances (
                ImageId=config['drop_ami'],
                MinCount=1, MaxCount=1,
                InstanceType=config['drop_type'],
                InstanceInitiatedShutdownBehavior=config['drop_terminate'],
                UserData=DROP_BOOT_SCRIPT,
                SecurityGroupIds=[config['drop_sec_group']],
                KeyName=config['drop_key'],
                TagSpecifications=[{
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Drop_Number',
                              'Value': str(i) }]
                }]
    )

