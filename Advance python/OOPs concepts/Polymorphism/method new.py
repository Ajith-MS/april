#Method over riding
class A:
    def printa(self):
        print("Inside class A")
class B(A):
    def printa(self):
        print("Inside class B")
class C(B):
    def printa(self):
        print("Inside class C")
ob=C()
ob.printa()

#
