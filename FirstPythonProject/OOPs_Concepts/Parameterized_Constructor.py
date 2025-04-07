class Dog:
    type = None
    name= None
    breed= None

    def bark(self):
        print('barking')

    def __init__(self, name, breed):        #Parameterized constructor creation
        print('This is Parameterized constructor')
        self.name=name
        self.breed=breed

chow_ref=Dog("Chow", "Mustafa")
mow_ref=Dog("Mow","Husky")

print(chow_ref.name,chow_ref.breed)

print(mow_ref.name,mow_ref.breed)