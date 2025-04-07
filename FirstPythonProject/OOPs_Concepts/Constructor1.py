#Passing input from constructor

class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a+self.b

    def diff(self):
        return self.a-self.b


    def mul(self):
        return self.a*self.b


    def div(self):
        return self.a/self.b


object_ref=calc(5,4)

Output_sum=object_ref.sum()
Output_diff=object_ref.diff()
Output_mul=object_ref.mul()
Output_div=object_ref.div()

print(Output_sum,Output_diff,Output_mul,Output_div)