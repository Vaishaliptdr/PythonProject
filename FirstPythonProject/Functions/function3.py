#Functions with return type
#a/b= proper division
#a%b= Gives remainder

####Print result in single variable
def maths_operations(a,b):
    return a+b,a-b,a*b, a/b, a%b


c=maths_operations(12,5)

print(c)     #Output: (17, 7, 60, 2.4, 2)



#####Print each result separately
def maths_operations1(a,b):
    return a+b,a-b,a*b, a/b, a%b


c,d,e,f,g=maths_operations1(12,5)

print(c)
print(d)
print(e)
print(f)
print(g)