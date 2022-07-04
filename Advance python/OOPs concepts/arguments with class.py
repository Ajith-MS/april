class Person():
    def setvalue(self,name,age,place):     #same value 2 functionil use cheyyan pattula
        self.name=name                     #instance keyword instance argument aaki mattan upayokikanath aan self keyword
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
pe1=Person()
pe1.setvalue("anu",26,"kochi")
pe1.printvalue()

pe2=Person()
pe2.setvalue("ajith",22,"varapuzha")
pe2.printvalue()

pe3=Person()
pe3.setvalue("deego",27,"cheanaloor")
pe3.printvalue()

