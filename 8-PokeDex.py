from PokeInfo import *
import json

myPokeDex = json.loads(data)
name = None
type = None

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
                        print(myPokeDex[type][pokemon])
                        foundPokemon = dict()
                        print("\n", pokemon.upper())      
                        for attribute in myPokeDex[type][pokemon]:
                            foundPokemon[attribute] = myPokeDex[type][pokemon][attribute]
                            print(attribute.capitalize(), ": ", foundPokemon[attribute])

                        name = input("\nSearch for another pokemon or type 'quit' to exit: ")                        
                        if not name == "quit":
                            PokeName()
                        else: 
                            print("\nOk, bye")
                            MainMenu()
                    if not name.lower() == pokemon.lower():
                        name = input("\nPokemon not found! Try again or type 'quit' to exit: ")                        
                        if not name == "quit":
                            PokeName()
                        else: 
                            print("\nOk, bye")
                            MainMenu()

        except:
            name = input("Pokemon not found! Try again or type 'quit' to exit: ")
            if name == "quit":
                print("\nOk, bye")
                MainMenu()
            else:
                PokeName()


def PokeType():
    global type
    if type == None:
        type = input("\nWhich type of pokemon do you want to buy today?:  ")
        type = type.upper()   
    try:
        n = 1
        print("I found", len(myPokeDex[type]),"Pokemons of", type, "type:\n")
        for pokemon in myPokeDex[type]:
            print(n, " - ",pokemon)
            n+=1
        
        checkAnswer1 = input("\nWanna check out the status of any of these?\n(Type pokemon's name to check its stats or 'quit' to exit):  ")
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
    name = input("\nType pokemon's name to see its stats: ")
    name = name.upper()
    print(name)
    PokeName()

def MainMenu():
    global name
    name = None
    action = input("What would you like to do?\n(Type only the option number)\n\n1 - Include Pokemon\n2 - Search by name\n3 - Search by type\n4 - Full list\nOption: ")
    try:
        int(action)
        if action == "1": 
            print("nice!")
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
        

PokeName()