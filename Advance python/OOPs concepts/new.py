#print on same function
class Add:
    def setnumber(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("sum of 2 numbers=",self.num1+self.num2)
sum=Add()
sum.setnumber(40,50)
