#Inheritance:-collecting the features of parent class by the child class (methods and variables)
#parent
#child

class A:                                    #parent_class , base_class , super_class
    def printa(self,num1):
        self.num1=num1
        print("Inside class A",self.num1)
class B(A):                                 #child_class , subclass ,derived_class
    def printb(self,num2):
        self.num2=num2
        print("Inside class B",self.num2,self.num1)
b=B()
b.printa(10)
b.printb(20)
