def add():
    sum=num1+num2
    print("Result =",sum)
def sub():
    min=num2-num1
    print("Result =",min)
def mul():
    multi=num1*num2
    print("Result =",multi)
def div():
    divi=num2/num1
    print("Result =",divi)

print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division ")
choice=int(input("Enter Your Choice :"))
num1=int(input("Enter Number 1 :"))
num2=int(input("Enter Number 2 :"))
if(choice==1):
    add()
elif(choice==2):
    sub()
elif(choice==3):
    mul()
elif(choice==4):
    div()
else:
    print("Invalid option !")

