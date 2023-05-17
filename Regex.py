data = "From daniel.albino14@gmail.com Sat Feb 14 16:20:00 2023"
#atIndex = data.find('@')
#print(atIndex)
#
#spcIndex = data.find(' ', atIndex)
#print(spcIndex)
#
#host = data[atIndex+1 : spcIndex]
#print(host)
#__________________________________________________________________
#words = data.split()
#email = words[1]
#pieces = email.split('@')
#print(pieces[1])
#__________________________________________________________________
import re
x = re.findall('^From .*@(\S*)', data)
print(x[0])