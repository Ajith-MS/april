#
class Person:
    def printp(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Student(Person):
    def prints(self,roll,dep):
        self.roll=roll
        self.dep=dep
        print(self.name,self.age,self.place,self.roll,self.dep)
stud=Student()
stud.printp("ajith",22,"varapuzha")
stud.prints(101,"Python")
