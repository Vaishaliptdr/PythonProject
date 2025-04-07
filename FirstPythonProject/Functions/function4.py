#function annotations

def maths_operations(a:int,b:int)-> int:
    return a+b

c=maths_operations(12,5)
print(c)


def maths_operations(a:str,b:str)-> str:
    return a+b
d=maths_operations('hi!! ','Hello')
print(d)