#Implementation of list

a=[1,2,3,4,4,1.4,3.5,'Ganesh']
print(a)

#Adding multiple values to list at a time
a+=['Radha',8,'y']   #Identical to a=a+['Radha',8]
#or
#a+='Radha',8,'y'

print(a)

print(a[6])  #Find the element according to index provided --->3.5

b=[2,3,4,[5,6]]
print(b)
print(b[3])
print(b[3][1])

c=[1,2,[3,4,[5,6,8,9]]]
print(c)
print(c[2])
print(c[2][2])
print(c[2][2][2])
