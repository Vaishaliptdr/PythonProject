# Here we are importing Module1 from package "FirstPythonProject"


from FirstPythonProject.Module.Module1 import greeting,guessing_game
from FirstPythonProject.Module.Module1 import test
from FirstPythonProject.Module.Module1 import name
from FirstPythonProject.Module.Module1 import __P
from FirstPythonProject.Module.Module1 import __display

greeting("Arnav")              #Functions
guessing_game(78)              #Functions

print(test.a)                  #Class

print(f'Hello, {name}')        #Variable

print(__P)                     #Private Variable

__display(200)                 #Private Function