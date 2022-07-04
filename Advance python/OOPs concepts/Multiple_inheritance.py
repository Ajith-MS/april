#Multiple inheritance
#child class inherits more than one parent class
class A:
    def printa(self):
        print("Inside class A")
class B:
    def printb(self):
        print("Inside class B")
class C(A,B):
    def printc(self):
        print("Inside class C")
ob=C()
ob.printc()
ob.printb()
ob.printa()