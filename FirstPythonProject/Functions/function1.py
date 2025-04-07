def greeting():
    print('Hello!!!!!!')

greeting()

def add():
    a=input('Enter the 1st number:')
    b=input('Enter the second number:')
    #input taken as string, we need to convert it to int for doing addition
    c=int(a)+int(b)
    print(f'Sum of numbers is {c}')

add()