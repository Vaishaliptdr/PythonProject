#Creating default constructor

class Dog:
    type = None
    name= None
    breed= None

    def bark(self):
        print('barking')

    def __init__(self):        #constructor creation
        print('Once object created I will be called')

chow=Dog()
mpw=Dog()
