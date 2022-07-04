#
salary=int(input("Enter the salary :"))
service=int(input("Enter service :"))
if(service>5):
    bonus=0.05*salary
    print("Your net bonus :",bonus)
else:
    print("You are not eligible")

