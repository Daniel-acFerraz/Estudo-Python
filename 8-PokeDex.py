from PokeInfo import *
import json
from PokeConstructor import Pokemon
import random
import re

myPokeDex = json.loads(data)
name = None
type = None

natures = ['Hardy', 'Bold', 'Modest', 'Calm', 'Timid', 'Lonely', 'Docile', 'Mild', 'Gentle', 'Hasty', 'Adamant', 'Impish', 'Bashful', 'Careful', 'Jolly', 'Naive', 'Brave', 'Relaxed', 'Quiet', 'Sassy', 'Serious']

def PokeInclude():
    newPokemon = Pokemon(input("Type the name of the pokemon would you like to register: ").capitalize(), input("Whats the type of this pokemon? ").capitalize())
    newPoke = dict()
    newPoke["type"] = newPokemon.type
    newPoke["level"] = random.randrange(40, 99)
    newPoke["IVs"] = random.randrange(8, 31)
    newPoke["Nature"] = random.choice(natures)   
    myPokeDex['FIRE'][newPokemon.name] = newPoke

    if re.search("fire", newPoke["type"].lower()):
        myPokeDex['FIRE'][newPokemon.name] = newPoke
        print("\nPokemon successfuly included in our system!\n")
    elif re.search("water", newPoke["type"].lower()):
        myPokeDex['WATER'][newPokemon.name] = newPoke
        print("\nPokemon successfuly included in our system!\n")
    elif re.search("grass", newPoke["type"].lower()):
        myPokeDex['GRASS'][newPokemon.name] = newPoke
        print("\nPokemon successfuly included in our system!\n")
    elif re.search("electric", newPoke["type"].lower()):
        myPokeDex['ELECTRIC'][newPokemon.name] = newPoke
        print("\nPokemon successfuly included in our system!\n")
    else:
        print("\nSorry, we're still not working with Pokemons os such type!")
    #with open('PokeInfo.py', 'a') as pokeData:
    #    pokeData.write(str(newPoke))
    print(newPokemon.name, newPoke)
    action = input("\nPress 'Enter' to add another pokemon or 'quit' to go to main menu: ")                        
    if action == "quit":
        MainMenu()
    elif action == "":
        PokeInclude()
    else:
        print("Invalid command, back to main menu")
        MainMenu()





def PokeName():
    global name
    if name == None:
        name = input("\nType the name of the pokemon you are looking for:  ").upper()
        PokeName()
    else:
        try:
            
            for type in myPokeDex:
                for pokemon in myPokeDex[type]:                    
                    if not name.lower() == pokemon.lower():
                        continue
                    else:
                        foundPokemon = dict()
                        print("\n", pokemon.upper())      
                        for attribute in myPokeDex[type][pokemon]:
                            foundPokemon[attribute] = myPokeDex[type][pokemon][attribute]
                            print(attribute.capitalize(), ": ", foundPokemon[attribute])

                        name = input("\nSearch for another pokemon or type 'quit' to go to main menu: ")                        
                        if not name == "quit":
                            PokeName()
                        else: 
                            print("\nOk, bye")
                            MainMenu()
                    if not name.lower() == pokemon.lower():
                        name = input("\nPokemon not found! Try again or type 'quit' to go to main menu: ")                        
                        if not name == "quit":
                            PokeName()
                        else: 
                            print("\nOk, bye")
                            MainMenu()

        except:
            name = input("Pokemon not found! Try again or type 'quit' to go to main menu: ")
            if name == "quit":
                print("\nOk, bye")
                MainMenu()
            else:
                PokeName()


def PokeType():
    global type
    if type == None:
        type = input("\nWhich type of pokemon are you looking for today?:  ")
        type = type.upper()   
    try:
        n = 1
        print("I found", len(myPokeDex[type]),"Pokemons of", type, "type:\n")
        for pokemon in myPokeDex[type]:
            print(n, " - ",pokemon)
            n+=1
        
        checkAnswer1 = input("\nWanna check out the status of any of these?\n(Type pokemon's name to check its stats or 'quit' to go to main menu):  ")
        if checkAnswer1.lower() == "quit":
            return print("\nOk, bye")
        else:
             global name
             name = checkAnswer1
             PokeName()
        
        
    except:
        print("\nSorry, currently we only have pokemons about the following types:\n")
        for types in myPokeDex:
            print(types)
        typeNotFound = input("\nYou can try again or type 'quit' to go to main menu:\n")
        if typeNotFound == "quit":
            return print("\nOk, bye")        
        else:
            type = typeNotFound.upper()
            PokeType()

def FullList():
    global name
    fullList = dict()
    for type in myPokeDex:
        for pokemonLower in myPokeDex[type]:
            pokemon = pokemonLower.upper()
            fullList[pokemon] = fullList.get(pokemon, myPokeDex[type][pokemonLower])
            print(pokemon, " - ", myPokeDex[type][pokemonLower]["type"])
    name = input("\nType pokemon's name to see its stats or 'quit' to go to main menu: ")
    name = name.upper()
    if name.lower() == "quit":
        print("\nOk, bye")
        MainMenu()
    else:
        PokeName()


def MainMenu():
    global name
    name = None
    action = input("What would you like to do?\n(Type only the option number)\n\n1 - Include Pokemon\n2 - Search by name\n3 - Search by type\n4 - Full list\nOption: ")
    try:
        int(action)
        if action == "1": 
            PokeInclude()
        elif(action == "2"): 
            PokeName()
        elif(action == "3"):
            PokeType()
        elif(action == "4"):
            FullList()
        else:
            print("\nNot a valid option\n")
            MainMenu()

    except:
        print("\nNot a valid option\n")
        MainMenu()
        
MainMenu()