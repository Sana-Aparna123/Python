age = 25 
name = "Aparna"
country = "India"
print("The person name is %s and age is %d and she is from %s " %(name,age,country))


#Using f-strings
print(f"The person name is {name} and age is {age} and she is from {country}")

quote1="Welcome to devsecops training - Python Module"
type(quote1)  #To check the type of the variable
dir(quote1) #To get the list of methods for string that can be used on the variable.


#To get length of the string
len(quote1) or quote1.__len__()

#Replace the specific words in a string using replace method
quote1.replace("devsecops","devops") #It will replace the word "devsecops" with "devops"

quote1.lower()#To convert the string to lower case
quote1.upper()#To convert the string to upper case
quote1.title()#To capitalize the first letter of each word
quote1.capitalize()#To capitalize the first letter of the string
quote1.casefold()#To convert the string to lower case
quote1.count("o")#count the number of occurences of a character in the string
quote1.swapcase()#Convert the lowercae to upper case and upper case to lower case

#Convert the string into Array or List
quote1.split() #By default it will split the string based on space
quote1.split("/") #It will split the string by delimeter "/". If the delimeter is not present in the string, it will return the entire string as a list.

#Removing the spacces from string
x='   Hello World...!  '
x.strip() #It will remove the leading and trailing spaces from the string
x.lstrip() #It will remove the leading spaces from the string
x.rstrip() #It will remove the trailing spaces from the string

#Join a friends using list or tuple
friends = ['John','Doe','Jane','Smith']
friends_str = "-".join(friends) #It will join the list elements with "-" as delimeter
print(friends_str)

#To check if the string starts with specific word
quote1.find("devsecops")
