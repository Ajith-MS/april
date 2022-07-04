class Person:
    def __init__(self):
        self.name="Ajith"           #public
        self.__age=22               #private
        self._place="Varapuzha"     #protected
    def printvalue(self):
        print(self.name)
        print(self.__age)
        print(self._place)

class Employee(Person):
    def __init__(self):
        Person.__init__(self)

    def printvalue(self):
        print()

ob=Employee()
ob.printvalue("Ajith",22,"Varapuzha",123,15000)