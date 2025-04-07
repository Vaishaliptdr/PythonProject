#We have imported Module from Module1 file and called its functions here
# We can import classes, variables, Private Variable, functions and Private Function

import Module1

Module1.greeting("Arnav")              #Functions
Module1.guessing_game(78)              #Functions

print(Module1.test.a)                  #Class

print(f'Hello, {Module1.name}')        #Variable

print(Module1.__P)                     #Private Variable

Module1.__display(200)                 #Private Function