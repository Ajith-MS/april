#Employee details with employee_name,designation,salary,company_name
#create class ,#2 functions with argument ,and 3 objects

class Employee:
    def setvalue(self,ename,desig,salary,cname):
        self.ename=ename
        self.desig=desig
        self.salary=salary
        self.cname=cname
    def printvalue(self):
        print(self.ename, self.desig, self.salary, self.cname)
em=Employee()
em.setvalue("aji","manager",100000,"google")
em.printvalue()

em1=Employee()
em1.setvalue("deego","manager",100000,"info")
em1.printvalue()
