counts = dict()
text = input("Enter a line of text here: ")
words = text.split()

print('Words: ',words)
print('counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
