#I want to take a list and remove duplicates from the list and convert it to tuple.
l=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
l1=set(l) #It will remove the duplicates from the list
print(tuple(l1)) #It will convert the set to tuple
#or
l1=list(set(l)) #It will remove the duplicates from the list
print(tuple(l1)) #It will convert the list to tuple

data=list(range(1,11))
print(data)
data.extend(range(1,11))
print(data)
set1=set(data)
print(tuple(set1)) #It will convert the set to tuple


#Set is a collection of unique elements.It is unordered and unindexed.
friends={'Rolf','ruth','charlie','Jen'}
friends.add('appu') #To add an single element to the set at the end
friends.pop() #To remove an element from the set
friends.remove('Rolf') #It will give an error if the element is not present in the set.
friends.discard('Rolf') #It will not give an error if the element is not present in the set.
friends.update({'rakesh','kiran'}) #It will add multiple elements to the set

friends1={'Rolf','ruth','charlie','Jen'}
friends2={'rakesh','kiran','appu','sri'}
friends1.update(friends2) #It will add the elements of friends2 to friends1
friends1.union(friends2) #It will add the elements of friends2 to friends1
friends1.intersection(friends2) #It will give the common elements between friends1 and friends2

#Frozenset
#A frozenset is an immutable set. It is a set that cannot be changed, just like a tuple.
#A frozenset is created using the function frozenset()
aws_regions=['us-east-1', 'us-west-1','ap-south-1','ap-southeast-1','eu-west-1'] 
frozen_set=frozenset(aws_regions)


#NoneType
#The None keyword is used to define a null value, or no value at all.
#None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.
p = 10
q = 20
r = print(p+q) #It will print the sum of p and q and return None
type(r) #It will return NoneType


# x=None
# if x is None:
#     print(x)
# else:
#     print(x)
    
# type(x) #It will return NoneType
    
#Output:None

x=20
if x is None:
    print(x)
else:
    print(x)
    
type(x) #It will return 20





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
        
        
vpcs = ec2_Client.describe_vpcs()
vpcs
vpcs.keys()
vpcs.get('Vpcs')
vpcs.get('Vpcs')[0]   #It will give the first element of the list
vpcs.get('Vpcs')[0]['VpcId'] #It will give the VPC ID of the first element of the list
vpcs.get('Vpcs')[0]['CidrBlock'] #It will give the CIDR block of the first element of the list

