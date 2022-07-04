#
class Student:
    def setvalue(self,name,rollno,dep,college):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.college=college
    def printvalue(self):
        print(self.name, self.rollno, self.dep, self.college)
su=Student()
su.setvalue("aji",1,"bca","jaibharath")
su.printvalue()

su1=Student()
su1.setvalue("deego",2,"mech","kmp")
su1.printvalue()

su2=Student()
su2.setvalue("steewo",3,"civil","kmm")
su2.printvalue()
