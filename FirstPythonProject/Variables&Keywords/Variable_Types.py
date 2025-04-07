a=10                            #Global Variable

class Person:
    b=11                        #Instance Variable  belongs to class

    def print_info(self):
        c = 30                  #Local Variable
        print(c)                # We can directly access local variable
        print(self.b)           # To access instance variable self needs to be used
        global a                # To access global variable a
        print(a)                # We can directly access global variable using 'global' keyword
        a= 'Hello!'             # Local variable will have priority as compared to global
        print(a)

Object_Ref=Person()
Object_Ref.print_info()
#Self is used to refer current object and is a first argument