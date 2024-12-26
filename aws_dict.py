import boto3
client = boto3.client('ec2',region_name='us-east-1')
vpc_raw = client.describe_vpcs().get('Vpcs', 'KeyNotFound')
type(vpc_raw) #list

for VPC in vpc_raw:
    print(VPC['VpcId'],'--------->',VPC.get('CidrBlock'))