#
class Employee:
    def printe(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print("Employee details :",self.name,self.age,self.place)
class Company(Employee):
    def printc(self,cname,desig,salary):
        self.cname=cname
        self.desig=desig
        self.salary=salary
        print("Details of employee in the company :",self.name,self.age,self.place,self.cname,self.desig,self.salary)
com=Company()
com.printe("Abilash",26,"kalamasery")
com.printc("CISCO","Manager",35000)

