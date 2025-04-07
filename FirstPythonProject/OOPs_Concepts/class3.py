from tkinter.font import names


class Person:
    name=None
    age=None

    def __init__(self,name):
        self.name=name


    def walk(self):
        return self.name

obj1=Person("Arnav")
obj2=Person("Aditya")

print(obj1.name)
print(obj2.name)
print('who is walking: ',obj1.walk())
print('who is walking: ',obj2.walk())




