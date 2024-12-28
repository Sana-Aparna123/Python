def func1():
    print("func1")
    
def func2():
    print("func2")
    
def func3():   
    print("func3")
    
    
class MyClass:
    def __init__(self):
        print("MyClass Constructor")
    def func1():
        print("func1")
    
    def func2():
        print("func2")

    def func3():
        print("func3")
        
        
        
#calling the function from the class
demo = MyClass
demo.func1()
demo.func2()
demo.func3()


class MyClass:
    def __init__(self):
        print("MyClass Constructor")
    def pokemon():
        import requests
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
        pokemon_list= pokemon.json().get('results')
        pokemon_name_list=[pk['name']  for pk in pokemon_list]
        return pokemon_name_list
    
    def func2():
        print("func2")

    def func3():
        print("func3")
        
x=MyClass
x.pokemon()
type(MyClass.pokemon) #pokemon