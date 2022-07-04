#Person:-name,age
#Child:-place,school
#Student:-roll,dep,college
class Person:
    def setpe(self,name,age):
        self.name=name
        self.age=age
class Child(Person):
    def setch(self,place,school):
        self.place=place
        self.school=school
class Student(Child):
    def setsu(self,roll,dep,collage):
        self.roll=roll
        self.dep=dep
        self.college=collage
        print(self.name,self.place,self.dep,self.college)
su=Student()
su.setpe("Ajith",22)
su.setch("Varapuzha","viswadeepti")
su.setsu(101,"BCA","Jaibharath")
