class Name:
    def __init__(self, *args):
        self.name, self.age = args 

    def _methodOne(self):
        print(f'Name methodOne()')

    def __str__(self):
        return f'Name: {self.name}  age: {self.age}'

class Student:
    def __init__(self):
        self.details = Name('Sachin', 51)

    def printDetails(self):
        print(f'Details {self.details}')
        self.details._methodOne() 


if __name__ == '__main__':
    obj = Student()
    obj.printDetails()