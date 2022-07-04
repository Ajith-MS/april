#Hiding the implementation details from the user.
#only the functionality will be provided to the user.
#advantages:-
#*increase security of application
#*reduce complexity
#abstract class:- the class  which has atleast own abstract method
#abstract method is the method which dont have body

from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def fun1(self):
        pass
    def fun2(self):
        print("This is the parent class")
class Child(Parent):
    def fun1(self):
        print("This is the child class")
ch=Child()
ch.fun1()
ch.fun2()

