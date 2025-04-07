#Another syntax to import functions from another file
# We can use alias for function name as well

from Module1 import greeting as g, guessing_game as game
from Module1 import name
from Module1 import test

g("Vaishali")
game(78)

print(f'My name is: {name}')
print(test.a)