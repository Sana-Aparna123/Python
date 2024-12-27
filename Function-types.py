'''They are diiferent ways you can  pass arguments to a function in Python.They are:
1.Re1quired arguments
2.Keyword arguments
3.Default arguments
4.Variable-length arguments'''


#Function with Default Arguments
#In below function we can call region as default argument.If we don't pass any value to region it will take us-east-1 as default value.
import boto3
def get_vpc(api='ec2',region='us-east-1'):
    if api == 'ec2':
        ec2_client=boto3.client('ec2',region_name=region)
        vpc_list=ec2_client.describe_vpcs().get('Vpcs')
        return vpc_list
    elif api == 's3':
        s3_client=boto3.client('s3',region_name=region)
        bucket_list=s3_client.list_buckets().get('Buckets')
        return bucket_list
    elif api == 'iam':
        iam_client=boto3.client('iam',region_name=region)
        user_list=iam_client.list_users().get('Users')
        return user_list
    else:
        print('Please provide valid API with EC2,S3 or IAM')
        return 'Invalid API'
    
#Calling the function with Default Arguments
get_vpc()



# import boto3
# def get_vpc(api='ec2',region='us-east-1'):
#     if api == 'ec2':
#         ec2_client=boto3.client('ec2',region_name=region)
#         vpc_list=ec2_client.describe_vpcs().get('Vpcs')
#         return [vpc['VpcId']  for vpc in vpc_list]
#     elif api == 's3':
#         s3_client=boto3.client('s3',region_name=region)
#         bucket_list=s3_client.list_buckets().get('Buckets')
#         return [bucket['Name'] for bucket in bucket_list]
#     elif api == 'iam':
#         iam_client=boto3.client('iam',region_name=region)
#         user_list=iam_client.list_users().get('Users')
#         return [user['UserName']for user in user_list]
#     else:
#         print('Please provide valid API with EC2,S3 or IAM')
#         return 'Invalid API'

import boto3
def get_vpc(api='ec2',region='us-east-1'):
    if api == 'ec2':
        ec2_client=boto3.client('ec2',region_name=region)
        vpc_list=ec2_client.describe_vpcs().get('Vpcs')
        for vpc in vpc_list:
            return vpc.get('VpcId')
    elif api == 's3':
        s3_client=boto3.client('s3',region_name=region)
        bucket_list=s3_client.list_buckets().get('Buckets')
        for bucket in bucket_list:
            return bucket.get('Name')
    elif api == 'iam':
        iam_client=boto3.client('iam',region_name=region)
        user_list=iam_client.list_users().get('Users')
        for user in user_list:
            return user.get('UserName')
    else:
        print('Please provide valid API with EC2,S3 or IAM')
        return 'Invalid API'
    
#Calling the function with Default Arguments
get_vpc()

#Using positional arguments
import boto3
def get_vpc(api,region):
    if api == 'ec2':
        ec2_client=boto3.client(api,region_name=region)
        vpc_list=ec2_client.describe_vpcs().get('Vpcs')
        return vpc_list
    elif api == 's3':
        s3_client=boto3.client(api,region_name=region)
        bucket_list=s3_client.list_buckets().get('Buckets')
        return bucket_list
    elif api == 'iam':
        iam_client=boto3.client(api,region_name=region)
        user_list=iam_client.list_users().get('Users')
        return user_list
    else:
        print('Please provide valid API with EC2,S3 or IAM')
        return 'Invalid API'

    

get_vpc('ec2','us-east-1')
#get_vpc('us-east-1','ec2') -->won't work
get_vpc(region='us-east-1',api='ec2') #will work


#Funtion with unknown number of arguments using *args
def hello(*actors):
    print(*actors)
    print(type(actors))
    for actor in actors:
        print(actor)
    
#Get VPC ID with unknown number of regions using *args
def vpc_id(*regions):
    for region in regions:
        ec2_client=boto3.client('ec2',region_name=region)
        vpc_list=ec2_client.describe_vpcs().get('Vpcs')
        print([vpc['VpcId'] for vpc in vpc_list])
        print('*'*100)
        
        
vpc_id('us-east-1','eu-west-1','ap-south-1')


#Function with unknown number of keyword arguments using **kwargs
def my_function(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
        
my_function(name='Aparna',age=23,city='Nellore')

#Give dynamodb full access permisiions to instance. using role.
# import boto3
# import uuid
# def dynamodb_table(**kwargs):
#         dynamodb_client=boto3.client('dynamodb',region_name='us-east-1')
#         uuid1=str(uuid.uuid4())
#         dynamodb_client.put_item(
#             TableName='devsecops-table',
#             Item={
#                 'uuid' : {'S':uuid1},
#                 'name' : {'S':kwargs.get('name')},
#                 'age' : {'N':str(kwargs.get('age'))},
#                 'city' : {'S':kwargs.get('city')}
#             } 
#         )
        
# dynamodb_table(name='Aparna',age=23,city='Nellore')


import boto3
import uuid
from faker import Faker
import random
data=Faker()
def dynamodb_table(**kwargs):
        dynamodb_client=boto3.client('dynamodb',region_name='us-east-1')
        uuid1=str(uuid.uuid4())
        dynamodb_client.put_item(
            TableName='devsecops-table',
            Item={
                'uuid' : {'S':uuid1},
                'name' : {'S':kwargs.get('name')},
                'age' : {'N':str(kwargs.get('age'))},
                'city' : {'S':kwargs.get('city')}
            } 
        )
        
dynamodb_table(name='Aparna',age=23,city='Nellore')
dynamodb_table(name=data.name(),age=data.random_int(min=18,max=100,step=1),city=data.city())
       
for x in range(10):
    dynamodb_table(name=data.name(),age=data.random_int(min=18,max=100,step=1),city=data.city())