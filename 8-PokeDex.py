from PokeInfo import *
import json

pokeInfo = json.loads(data)

def PokeType(type = input("Which type of pokemon do you want to analyse today?\n")):
    type = type.upper()
    n = 1
    try:
        print("I found", len(pokeInfo[type]),"Pokemons of", type, "type:\n")
        for pokemon in pokeInfo[type]:
            print(n, " - ",pokemon)
            n+=1
        def pokemonSelector(pokeNumber = input("\nWanna check out the status of any of these?\n(Type pokemon's number to check or 'no' to quit)\n")):
            print(pokeNumber)
        
    except:
        print("Sorry, currently we only have data about the following types:\n")
        for types in pokeInfo:
            print(types)
        typeNotFound = input("\nYou can try again or type 'quit' to go to main menu:\n")
        if typeNotFound == "quit":
            return print("Ok, bye")
        
        else:
            type = typeNotFound
            PokeType(type)   
            

#print(info)

PokeType()