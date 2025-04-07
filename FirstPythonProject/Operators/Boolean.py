# and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('-------------------------------------------------')

# or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('-------------------------------------------------')

a=10
b=20
c=30

print(a<10 and b<20 and c<30)
print(a<10 and b==20 and c==30)
print(a<10 and b<20 or c==30)

print('-------------------------------------------------')

print((a<10 and b<20) and c<30)
print(a<10 and (b==20 and c==30))
print((a<10 and b<20) or c==30)

#Operations from parenthesis are executed first