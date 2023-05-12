from StudentConstructor import Student
from ForeignStudent import ForeignStudent

mike = Student("Mike Dane", "TI", 4.9, True)
ana = Student("Ana Maria", "HR", 3.1, False)
aliBaba = ForeignStudent("Ali Baba", "Engeneering", 4.2, True)

print(mike.name, mike.gpa, mike.isOnHonorRoll())
print(ana.name, ana.gpa, ana.isOnHonorRoll())
print(aliBaba.nationality("muslim"))