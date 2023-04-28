fileName = 'text.txt'
handlef = open(fileName)
count = dict()

for line in handlef:
    words = line.split()    
    for word in words:
        count[word] = count.get(word, 0) + 1

myList = list()
for k,v in count.items():
    myList.append((v,k))

myList = sorted(myList, reverse=True)

for v,k in myList[:5]:
    print(k,v)