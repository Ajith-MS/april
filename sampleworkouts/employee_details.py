#empname,age,salary,cname,designation

class Employee:
    def setvalues(self,empname,age,salary,cname,desig):
        self.empname=empname
        self.age=age
        self.salary=salary
        self.cname=cname
        self.desig=desig
    def printvalues(self):
        print(self.empname,",",self.age,",",self.salary,",",self.cname,",",self.desig)
emp=Employee()
emp.setvalues("Arun",25,35000,"Infopark","Java developer")
emp.printvalues()

emp1=Employee()
emp1.setvalues("Akhil",24,30000,"CISO",".net developer")
emp1.printvalues()

emp2=Employee()
emp2.setvalues("Akshay",28,40000,"Google","Php developer")
emp2.printvalues()

emp3=Employee()
emp3.setvalues("Ajith",22,100000,"Google","Manager")
emp3.printvalues()

emp4=Employee()
emp4.setvalues("Deego",27,50000,"Infopark","Python developer")
emp4.printvalues()