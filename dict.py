
aws_cloud = {
    'name' : 'Amazon Web Services',
    'parent' : 'Amazon',
    'founded' : 2006,
    'founder' : 'Jeff Bezos',
    'headquarters' : 'Seattle, Washington, U.S.',
    'services' : ['EC2','S3','RDS','Lambda','Route 53','IAM','VPC'],
    'still_active' : True
    
}

type(aws_cloud) #dict
aws_cloud.keys() #It will give the list of keys in the dictionary
aws_cloud.values() #It will give the list of values in the dictionary
aws_cloud.items() #It will give the list of key-value pairs in the dictionary
aws_cloud.popitem() #It will remove the last key-value pair from the dictionary
aws_cloud.pop('founded') #It will remove the key-value pair from the dictionary using by key
aws_cloud.get('services') #It will give the value of the key
aws_cloud['services'] #It will give the value of the key
aws_cloud['services'][0] #'EC2'
aws_cloud['services'][1] #'S3'
aws_cloud.update({"Others":["whole foods","Blue Origin","Twitch"]}) #It will add the new key-value pair to the dictionary
aws_cloud.clear() #It will clear the dictionary and give empty dictionary

#Create a dictionary using two lists
x=list(range(1,5))
y=['a','b','c','d','e']
z=dict(zip(x,y)) #It will create a dictionary using two lists


#Create a dictionary using fromkeys method
x=list(range(1,5))
newdict=dict.fromkeys(x,'default')
print(newdict)


x=list(range(1,5))
y=['us-east-1', 'us-west-1','ap-south-1','ap-southeast-1','eu-west-1'] 
z=dict(zip(x,y))

z.setdefault(5,'us-east-2') #It will add the key-value pair to the dictionary if the key is not present and return the value
z.setdefault(1,'us-east-2') #If key is present i wont add new key and value .It will return the existing value for the key.

#Looping through a dictionary
for key,value in aws_cloud.items():
    print(f"Key: {key} ---> Value: {value}")
    
for k,v in aws_cloud.items():
    print(f"{k} --> {v}")
