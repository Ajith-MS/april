#Mobile details ,2 functions with argument ,5 objects
class Mobile:
    def svalues(self,mname,cname,price,ofrprice):
        self.mname=mname
        self.cname=cname
        self.price=price
        self.ofrprice=ofrprice
    def pvalues(self):
        print(self.mname," ",self.cname," ",self.price," ",self.ofrprice)
mob=Mobile()
mob.svalues("Iphone 13 pro","apple",65000,63000)
mob.pvalues()

mob1=Mobile()
mob1.svalues("redmi note 5 pro","mi",14000,12000)
mob1.pvalues()

mob2=Mobile()
mob2.svalues("reno 4 pro","oppo",25000,22000)
mob2.pvalues()

mob3=Mobile()
mob3.svalues("Iphone 12 pro","apple",55000,52000)
mob3.pvalues()

mob4=Mobile()
mob4.svalues("j5s","samsung",18000,15000)
mob4.pvalues()