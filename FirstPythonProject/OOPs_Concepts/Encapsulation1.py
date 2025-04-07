#Encapsulation :
# Hiding data members(Class variables, instance variable by using only the methods __)
#There is no private keyword in Python, we need to use __ symbol
#Private variable can be only accessed through the functions

class car:
    def __init__(self):
        self.password='Pass123'             #public instance variable
        self.__secure_password='P@ssword'   #private instance variable

    def __private_function(self):
        print('I am private function')

    def change_password(self):
        self.password='changed'
        self.__secure_password='890'   #we can access private variable from function of that class
        print(self.password)
        print(self.__secure_password)
        self.__private_function()    #private function can be called from public function



obj=car()
print(obj.password)
#print(obj.__secure_password)     #car class do not have access to secure_password as it is made private using (__)

obj.change_password()
#obj.__privat_function()         #private functions can not be accessed outside class, to access private variable we need to call them from public function