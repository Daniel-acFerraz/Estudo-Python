fileName = 'text.txt'
handleF = open(fileName, 'r')
#print(handleF.read())

count = dict()
for line in handleF:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

bigCount = None
bigWord = None
for word,count in count.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word
print(bigWord, bigCount)