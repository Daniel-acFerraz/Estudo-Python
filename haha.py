from PokeConstructor import Pokemon

newPokemon = Pokemon("bulbassaur", "grass", 80, "35", "Bold")

newPoke = dict()
newPoke["name"] = newPokemon.name
newPoke["type"] = newPokemon.type
newPoke["level"] = newPokemon.level
newPoke["IVs"] = newPokemon.IVs
newPoke["Nature"] = newPokemon.Nature

print(newPoke)