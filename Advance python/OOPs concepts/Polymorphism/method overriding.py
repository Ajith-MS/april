#Method overriding
#Same method name and same number of arguments
#child class parent classine override cheyyum
#latest method call cheyyollu
class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("Inside class Add :",self.num1+self.num2)
class Add1(Add):
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("Inside class Add1 :",self.num1+self.num2)
ob=Add1()
ob.sum(15,25)