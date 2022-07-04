#name ,roll, age ,institution_name,fees

class Luminar:
    i_name='luminar technolab'
    fees=29500
    def setvalues(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalues(self):
        print(self.name,self.roll,self.age,Luminar.i_name,Luminar.fees)
lum=Luminar()
lum.setvalues("Ajith",101,22)
lum.printvalues()

lum1=Luminar()
lum.setvalues("Deego",102,27)
lum.printvalues()

lum2=Luminar()
lum2.setvalues("Steewo",103,24)
lum2.printvalues()