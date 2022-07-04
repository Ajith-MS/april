class Employee:
    def __init__(self,id,fname,lname,age,prof,country):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.country=country
    def printe(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.country)
f=open("D:\Dont delete windows files\Downloads\customer","r")
lst=[]
for i in f:
    data=i.rstrip("\n").split(',')
    id=data[0]
    fname=data[1]
    lname=data[2]
    age=data[3]
    prof=data[4]
    country=data[-1]
    ob=Employee(id,fname,lname,age,prof,country)
    lst.append((ob.fname,ob.lname,ob.age,ob.prof))
print(lst)