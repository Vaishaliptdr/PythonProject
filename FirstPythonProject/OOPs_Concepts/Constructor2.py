class Car:
    def __init__(self, brand, doors, wheels=4 ):  #we can provide default value for any parameter
        self.brand=brand
        self.doors=doors
        self.wheels=wheels
        print('Hi, I am new car, My name is: '+brand, +doors, +wheels)

car1=Car("bmw",4)
car2=Car("baleno", 4,5)   #we can change default value of parameter while calling object




