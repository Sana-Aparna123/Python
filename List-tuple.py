aws_regions=['us-east-1', 'us-west-1','ap-south-1','ap-southeast-1','eu-west-1']
print(aws_regions)


#list methods
aws_regions.append('eu-central-1') #It will add the element at the end of the list
aws_regions.insert(2,'ap-northeast-1') #It will add the element at the specific index
aws_regions.pop() #It will remove the last element from the list
aws_regions.pop(2) #It will remove the element from the specific index
aws_regions.remove('us-west-1') #It will remove the specific element from the list
aws_regions.reverse() #It will reverse the list
aws_regions.clear() # It will clear the list and give empty list
aws_regions.sort() #It will sort the list in ascending order
aws_regions.sort(reverse=True) #It will sort the list in descending order
aws_regions.count('us-east-1') #It will count the number of occurences of the element in the list


#extend method
x=[1,2,3]
y=[4,5,6]
x.extend(y) #It will add the elements of y list to x list or add new list to existing list


#Note:
new_regions_list1=aws_regions
id(new_regions_list1) #To copy a list with reference means if we chang the new_regions_list1, it will also change the aws_regions.
id(aws_regions) #To get the memory location of the variable

new_regions_list2=aws_regions.copy() #To create a copy of the list
id(new_regions_list2) #To copy a new list without reference means if we change the new_regions_list2, it will not change the aws_regions.
id(aws_regions) #To get the memory location of the variable



#Tuple
aws_regions1=('us-east-1', 'us-west-1','ap-south-1','ap-southeast-1','eu-west-1')
print(aws_regions1)
type(aws_regions1)
aws_regions1.count('us-east-1') #It will count the number of occurences of the element in the tuple
aws_regions1.index('us-east-1') #It will give the index of the element in the tuple

import sys
sys.getsizeof(aws_regions) #To get the size of the list 152 in bytes
sys.getsizeof(aws_regions1) #To get the size of the tuple 80 in bytes


#range
range(10) #It will give the range from 0 to 9
range(1,10) #It will give the range from 1 to 9
range(1,10,2) #It will give the range from 1 to 9 with step 2
list(range(10)) #It will convert the range to list with range from 0 to 9



#Examples:
#Attach the ec2 iam policy to instance then only it will work.
#Get the VPC ID's from the AWS regions using list
#pip install boto3   --> library to connect to AWS
# dir(boto3)  --> To get the list of methods that can be used with boto3
# import boto3
# aws_regions=['us-east-1', 'us-west-1','ap-south-1','ap-southeast-1','eu-west-1'] 
# for region in aws_regions:
#     ec2_Client=boto3.client('ec2',region_name=region)
#     vpc_list=ec2_Client.describe_vpcs().get('Vpcs',[])
#     for vpc in vpc_list:
#         print(f"VPC ID in {region} is {vpc.get('VpcId')}")


#Using List
import boto3
aws_regions=['us-east-1', 'us-west-1','ap-south-1','ap-southeast-1','eu-west-1'] 
for region in aws_regions:
    region_vpc=[]
    ec2_Client=boto3.client('ec2',region_name=region)
    vpc_list=ec2_Client.describe_vpcs().get('Vpcs',[])
    for vpc in vpc_list:
        region_vpc.append(vpc.get('VpcId'))
        print(f"Lets gets print the vpc for region {region} ")
        print(region_vpc)
        print('-'*150)
        
        
        
#Using Tuple
import boto3
aws_regions=('us-east-1', 'us-west-1','ap-south-1','ap-southeast-1','eu-west-1') 
for region in aws_regions:
    region_vpc=[]
    ec2_Client=boto3.client('ec2',region_name=region)
    vpc_list=ec2_Client.describe_vpcs().get('Vpcs',[])
    for vpc in vpc_list:
        region_vpc.append(vpc.get('VpcId'))
        region_vpc_tuple=tuple(region_vpc)
        print(f"Lets gets print the vpc for region {region} ")
        print(region_vpc_tuple)
        print('-'*150)





