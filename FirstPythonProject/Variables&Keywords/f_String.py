# Working with variables
# Concatenating String with f-string

a=6
print(a)

print(a+4)

b='Hello!!'
c='Vaishali'
print(b)

# print(b+4)   Error as can not add integer to string

print(b*3)   # Prints the string 3 times

#String Concatenation
print(b + " " + ' world!')   # Integer + String
print(b+" "+c)                   # String + string

# Variables can be updated in between the code

c= 'Keshav'
print(b+" "+c)

x='Hello!'
y='Arnav'
z='Aditya'

concat_python_way=f'{x} {y} {z}'
print(concat_python_way)
print(f'{x} {concat_python_way}')



