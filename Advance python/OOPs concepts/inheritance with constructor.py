#
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Student(Person):
    def __init__(self,name,age,place,rollno,dep,college):
        super().__init__(name,age,place)
        self.rollno=rollno
        self.dep=dep
        self.college=college
        print(self.name,self.age,self.place,self.rollno,self.dep,self.college)
ob=Student("Ajith",22,"varapuzha",101,"BCA","jaibharath")
