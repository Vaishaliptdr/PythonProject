# Module is python file that contain functions that can be reused in other file
# We have stored functions in this file and we will call it from another file Module2.py

def greeting(name):
    print(f'Hello!, {name}')

class test:
    a=67

name="Keshav"
__P=90

def guessing_game(number):
    user_input = ''
    while user_input != '-1':
        user_input = input("\nEnter number:")
        if int(user_input) == number:
            print("Bingo! You guessed correct number ")
        print(f'number is {user_input} Try again......')

def __display(value):
    print(f'The value is: {value}')


