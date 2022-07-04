class Parent:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Student(Parent):
    def __init__(self,rollno,dep,college,name,age,place):
        super().__init__(name,age,place)
        self.rollno=rollno
        self.dep=dep
        self.college=college
        print(self.name,self.age,self.place,self.rollno,self.dep,self.college)
ob=Student("Ajith MS",22,"Varapuzha",101,"BCA","Jaibharath")