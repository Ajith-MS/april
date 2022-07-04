#
numcls=int(input("Total number of class held :"))
numatt=int(input("Total number of class attended :"))
percentage=(numatt/numcls)*100
if(percentage>75):
    print("Eligible to sit in the class")
else:
    print("Not eligible to sit in the class")