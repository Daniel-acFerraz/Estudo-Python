
from PokeInfo import *
import json
from PokeConstructor import Pokemon
import random
import re

myPoke = dict()
myPoke["type"] = "Grass and psychic"


if re.search("grass", myPoke["type"].lower()):
    print("yeah")