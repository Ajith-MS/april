#multiple inheritance with constructor

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Employee:
    def __init__(self,id,dep,salary):
        self.id=id
        self.dep=dep
        self.salary=salary
class Student(Person,Employee):
    def __init__(self,roll,college,name,age,place,id,dep,salary):
        Person.__init__(self,name,age,place)
        Employee.__init__(self,id,dep,salary)
        self.roll=roll
        self.college=college
        print(self.name,self.age,self.place,self.id,self.dep,self.salary,self.roll,self.college)
ob=Student("Ajith",22,"varapuzha",101,"BCA",50000,180021094113,"jaibharath")

