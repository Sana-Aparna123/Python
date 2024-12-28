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


#Run these commands in jupyter notebook
import pandas as pd

df = pd.read_csv('london_houses.csv')

df
df.shape # Provides tuple of (Rows,Cols)
df.info() # Provids Dataset Information
df.columns # Provides all cols information
df.head() # give first 5 rows information
df.head(10) #gives first 10 rows information
df.tail() # gives last 5 rows information
df.tail(10) # gives last 10 rows information
df['Neighborhood'].head(10) #Prints only Neighborhood Col Information for 10 Rows
#Choosing Multiple Cols
df[['Neighborhood','Bedrooms','Bathrooms']].head(10) #Prints only Neighborhood,Bedrooms,Bathrooms Col Information for 10 Rows


df.loc
df.iloc[0:3] #Prints Rows with Index 0,1,2


#Chaning the Index Col
df = pd.read_csv('london_houses.csv',index_col='team')


#Finding the Goals Scored by Uruguay Team.
df.loc['Uruguay']
df.loc['Uruguay']
df.loc['Chile']
df.loc['Chile'][4:10]


df['minute'] > 44.0 # Displays only True or False


min1 = df['minute'] > 44.0
df[min1]


min2 = (df['minute'] > 44.0 & df['minute'] < 80)
