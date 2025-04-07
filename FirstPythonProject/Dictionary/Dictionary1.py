# Dictionary represented by {}
# Mentioned in the form of key-value pair
# Dict={"Key":"Value"}
# Key can be integer, string, double,tuple
# Values can be anything
# Fastest as compared to list and tuples

a={"name":"Vaishali", "age": 26, "College":"MET"}
print(a)
print("--------------------------------------------------------------")
b={"name":"Keshav",3.14:"pi", "List":[1,2,3.9,'Arnav'], "tuple":(2,'t',9.8),"dict":{2,'y',7.6}}
print(b)

print("--------------------------------------------------------------")
print(a.values())                   #Prints the values of dictionary
print(a.keys())                     #Prints the Keys of dictionary
print(a.pop("College"))             #Pops out the key-value pair according to provided key
print(a)
b.popitem()                         #Pops out last item from dictionary
print(b)
print("--------------------------------------------------------------")

print(a.get("age"))                 #We can get the value of mentioned key
print(a.items())                    #Prints the items of dictionary

a.update({'College':"AICTE",'age':67})   #Updates previous info or add new info
print(a)
