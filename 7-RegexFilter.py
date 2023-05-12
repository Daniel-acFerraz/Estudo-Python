import re
handlef = open('Text.txt')
numList = list()
#for line in handlef:
#    line = line.rstrip()
#   numbers = re.findall('^X-DSPAM-CONFIDENCE: ([0-9.]+)', line)
#   if len(numbers) < 1 : continue
#    number = float(numbers[0])
#    numList.append(number)
#print('Maximum spam ping: ', max(numList))

xboxPrice = list()
for line in handlef:
    line = line.rstrip()
    prices = re.findall('^X-BOX.+: (\$[0-9.]+)', line)
    if len(prices) < 1 : continue
    xboxPrice.append((prices))
print('The cheapest X-box costs: ', min(xboxPrice))
