#Sample Function

# import boto3
# def get_s3_bucket_list():
#     s3_client=boto3.client('s3',region_name='us-east-1')
#     bucket_list=s3_client.list_buckets().get('Buckets')
#     for bucket in bucket_list:
#         print(bucket.get('Name'))

# get_s3_bucket_list()


import boto3
def get_s3_bucket_list():
    bucket_list1=[]
    s3_client=boto3.client('s3',region_name='us-east-1')
    bucket_list=s3_client.list_buckets().get('Buckets')
    for bucket in bucket_list:
        bucket_list1.append(bucket.get('Name'))
    return bucket_list1



my_buckets=get_s3_bucket_list()
my_buckets
type(my_buckets) #list
my_buckets.sort()

for b in my_buckets:
    print(b)


#Using List Comprehension
import boto3
def get_s3_bucket_list():
    s3_cliet=boto3.client('s3',region_name='us-east-1')
    all_buckets=s3_cliet.list_buckets().get('Buckets')
    bucket_list=[bucket['Name']  for bucket in all_buckets]
    return bucket_list

my_buckets=get_s3_bucket_list()
my_buckets

#Using normal for loop
for buckets in my_buckets:
    print(buckets)

#list comprehension
list=[buckets for buckets in my_buckets]
list
        
    

# import boto3
# import json
# def get_s3_bucket_list():
#     s3_client=boto3.client('s3',region_name='us-east-1')
#     res=s3_client.list_buckets().get('Buckets')
#     n=json.dumps(res,indent=4)
#     print(n)
    