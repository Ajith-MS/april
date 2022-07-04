#person:-name,
class Person:
    def setpe(self,name,age):
        self.name=name
        self.age=age
class Parent:
    def setpa(self,place,phno):
        self.place=place
        self.phno=phno
class Employee(Person,Parent):
    def setem(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
        print(self.name,self.age,self.place,self.phno,self.id,self.desig,self.salary)
em=Employee()
em.setpe("ajith",22)
em.setpa("varapuzha",9526155487)
em.setem(101,"python developer",55000)