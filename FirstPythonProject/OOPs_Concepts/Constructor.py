#taking user input from console

class calc:
    def __init__(self):
        print('I am default')

    def __int__(self,a,b):
        print('I am parameterized')

    def sum(self,a,b):
        return a+b

    def diff(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

object_ref=calc()
a=float(input('Enter first number: '))
b=float(input('Enter second number: '))

Output_sum=object_ref.sum(a,b)
Output_diff=object_ref.diff(a,b)
Output_mul=object_ref.mul(a,b)
Output_div=object_ref.div(a,b)

print(Output_sum,Output_diff,Output_mul,Output_div)




