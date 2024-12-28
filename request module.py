#request module  is used to send all kinds of HTTP requests. It is an easy-to-use library with a lot of features ranging from passing parameters in URLs to sending custom headers and SSL Verification.
#request module is used to connect with api's and get the data from the api's.
import requests
pokemon = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
pokemon.json()
pokemon.json().get('results')


#if i need names in it
import requests
pokemon = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
pokemon_list= pokemon.json().get('results')
pokemon_name_list=[pk['name']  for pk in pokemon_list]  
len(pokemon_name_list) #1302
#pokemon_name_list=[pk['url']  for pk in pokemon_list]
print(pokemon_name_list)


  
#Modules
'''
1.boto3
2.Faker
3.Json,os,sys,random,math
4.virtual Environment
5.Requests
6.Pandas
7.Jupyter Notebooks
8.Regular Expressions  ''' 