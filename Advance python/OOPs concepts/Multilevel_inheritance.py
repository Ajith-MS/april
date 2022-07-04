#Multilevel inheritance
class A:
    def seta(self):
        print("Inside class A")
class B(A):
    def setb(self):
        print("Inside class B")
class C(B):
    def setc(self):
        print("Inside class C")
ob=C()
ob.seta()
ob.setb()
ob.setc()
