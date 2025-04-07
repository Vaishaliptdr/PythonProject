#Creating class
# Class will not get memory but once object is created memory will get
# assigned to that class

class vehicle:
    # Attributes/Instance Variable/Data Variable
    wheels=4
    color='gray'

    #Creating function inside class
    # self is used to refer own object reference

    def print_color(self):
        print(v1.color)
        print(v1.wheels)

    def pass_function(self):
        pass                                  #Empty function

v1=vehicle()  #Object creation

v2=vehicle()
print(v2.color)

print('------------------------------------')
#Calling function
v1.print_color()