from StudentConstructor import Student

class ForeignStudent(Student):

    def nationality(self, nationality):
        print(self.name + " is a " + nationality)