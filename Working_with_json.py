#Python json module has two methods:
#json.dumps() - To convert the python object  to a JSON string
#json.dump() - To write a python object to a JSON file
#json.loads() - To convert the JSON string to a python object.
#json.load() - To read the JSON file and convert it to a python object.

import json

aws_cloud = {
    'name' : 'Amazon Web Services',
    'parent' : 'Amazon',
    'founded' : 2006,
    'founder' : 'Jeff Bezos',
    'headquarters' : 'Seattle, Washington, U.S.',
    'services' : ['EC2','S3','RDS','Lambda','Route 53','IAM','VPC'],
    'still_active' : True
    
}

x = json.dumps(aws_cloud) #It will convert the python object to a JSON string
y = json.loads(x) #It will convert the JSON string to a python object




