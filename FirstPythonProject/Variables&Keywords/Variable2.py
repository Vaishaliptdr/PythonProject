#Local and Global Variable

b=20           #Global Variable
c=30
print(c)

def f():
    a=10       #Local Variable
    print(a)
    global c    #Calling global variable
    c=40        #updating global variable
    print(c)
f()

print(b)
print(c)   # Update value will be printed
#print(a)   #-----Error as outside function