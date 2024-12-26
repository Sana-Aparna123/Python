#Python file handling can be done in two ways
#1. Using open() function
#2. Using with open() function

#Using open() function --> old way
#login into server and store some data in 'data' file 
#cd /tmp/
#nano data

f = open('/tmp/data') or f=open('/tmp/data','rt') #Both are same
f.readlines()
f.close()

f = open('/tmp/data')
f.readline()
f.close()

#Output will be in json format
from faker import Faker
import json
data = Faker()
f = open('/tmp/profiles','wt')
profile=data.profile()
json_profie=json.dumps(profile,default=str,indent=2)
f.write(str(json_profie))
f.close()

#Output will be in dictionary format
from faker import Faker
import json
data = Faker()
f = open('/tmp/profiles','wt')
profile=data.profile()
f.write(str(profile))
f.close()


#Using with open() function --> new way
from faker import Faker
import json
data = Faker()
with open ('/tmp/profiles','wt') as f:
    profile=data.profile()
    json_profie=json.dumps(profile,default=str,indent=2)
    f.write(str(json_profie))
    f.close()


from faker import Faker
import json
data = Faker()
with open ('/tmp/profiles',"a+") as f:
    profile=data.profile()
    json_profie=json.dumps(profile,default=str,indent=2)
    f.write(str(json_profie))
    f.close()
#a+ --> append mode


#Using json.dump() to write a file
from faker import Faker
import json
data = Faker()
with open ('/tmp/jsondump',"a+") as f:
    profile=data.profile()
    json.dump(profile,f,default=str,indent=2)
    f.close()

#cat /tmp/profiles

with open ('/tmp/ip.json',"r") as f:
    x=str(f.readlines())
    print(x)
    
#Imagine if i have a file with json data and i need to read it and convert it to python object,I can use the json.load() method.
#Loading a JSON file and converting it to a python object
import json
with open ('/tmp/ip.json',"r") as f:
    x=json.load(f)
    print(x)
    
    
    
import json
with open ('/tmp/ip.json',"r") as f:
    x=json.load(f)
    print(x.keys())
    for item in x['values']:
        print(item)
    
    
#To convert the JSON string to a python object
import json
aws_cloud = '''{
    "name": "Amazon Web Services",
    "parent": "Amazon",
    "founded": 2006,
    "founder": "Jeff Bezos",
    "headquarters": "Seattle, Washington, U.S.",
    "services": ["EC2", "S3", "RDS", "Lambda", "Route 53", "IAM", "VPC"],
    "still_active": true
}'''

json.loads(aws_cloud)
    
    
    
    