
#To do this remove ec2 and s3 role access to instance then only it will give exception.
import boto3
from botocore.exceptions import ClientError,NoCredentialsError,NoRegionError,EndpointConnectionError
def get_vpcs(region):
    try:
        ec2_client=boto3.client('ec2',region_name=region)
        vpc_list=ec2_client.describe_vpcs().get('Vpcs')
        vpcs = [vpc['VpcId'] for vpc in vpc_list]
        print(vpcs)
        return vpc_list
    except NoRegionError as e:
        print("Error:",e)
    except NoCredentialsError as e:
        print("Error:",e)
    except ClientError as e:
        print("Error:",e)
    except EndpointConnectionError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)
    finally:
        print("Execution Completed")
        return "Execution Completed."
 
  
#Try this one before executing the above code.It will unable to locate credentials.     
import boto3
def get_vpc():
    ec2_client=boto3.client('ec2',region_name='us-east-1')
    vpc_list=ec2_client.describe_vpcs().get('Vpcs')
    for vpc in vpc_list:
        return vpc.get('VpcId')
