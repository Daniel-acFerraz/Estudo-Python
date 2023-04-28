myDict = {'a': 1, 'b': 13, 'c': 22}

#myList = list()
#for k, v in myDict.items():
#    myList.append((v, k))
#
#myList = sorted(myList, reverse=True)
#print(myList)

print(sorted([(v,k) for k,v in myDict.items()], reverse=True))

