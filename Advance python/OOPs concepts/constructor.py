# Constructor:-to define instace variable in an object
#syntax:-__init

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalues(self):
        print(self.name,self.age,self.place)
p1=Person("Ajith",22,"Varapuzha")
p1.printvalues()

p2=Person("Arun",24,"Kongorpilly")
p2.printvalues()

p3=Person("Deego",27,"Cherannaloor")
p3.printvalues()
