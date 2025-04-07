#Functions with arguments

def greeting(name):
    print(f'Hello!, {name}')

greeting('Arnav')
greeting('Aditya')

def guessing_game(number):
    user_input = ''
    while user_input != '-1':
        user_input = input("\nEnter number:")
        if int(user_input) == number:
            print("Bingo! You guessed correct number ")
        print(f'number is {user_input} Try again......')

guessing_game(89)