#When range is known then for loop is used

for i in "Hello!":
    print(i)

for i in range(6):
    print(i)

list=["Arnav", "Aditya", "Anu","Aarush"]
for i in list:
    print(i)
    print(f'Hello,{i}')


list=["Arnav", "Aditya", "Anu","Aarush"]
for i in list:
    print(f'Hello,{i}')
    if i=="Anu":
        print(f'{i} is a girl')
    else:
        print("Hello...........")