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


#Installing the pandas and jupyter notebook
# pip3 install pandas
# pip3 install jupyterlab
# python3 -m jupyterlab --allow-root --ip=10.43.1.217 --> private ip of ec2 machine (It will give on url)
#Access the below url in browser
#  http://34.205.69.155:8888/lab?token=3a0f59cde4b9fcd0681fcf26cae44e1604440aa2168bef31-->here give the public ip of ec2 machine

#we can use jupyter for csv files,excel files,sql files,python files etc.
#Kaggle is a web platform that's a community for data scientists and machine learning practitioners.
#It's a platform where you can find datasets, participate in competitions, and collaborate with other data scientists.
#london_houses.csv(129.5 kB)  --> dataset from kaggle (download it)-->Houses in London dataset
#Using pandas we can manipilate the above csv file data.