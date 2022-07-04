#1.Addition
#2.Subtraction
#3.Multiplication
#4.Division

#Enter your choice:
#num1
#num2
def add():
    add=num1+num2
    print(num1,"+",num2,"=",add)
def sub():
    sub=num1-num2
    print("Result =",sub)
def mul():
    mul=num1*num2
    print("Result =",mul)
def div():
    div=num2/num1
    print("Result =",div)
print(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division ")
choice=int(input("Enter your choice :"))
num1=int(input("Enter Number1 :"))
num2=int(input("Enter Number2 :"))
if(choice==1):
    add()
elif(choice==2):
    sub()
elif(choice==3):
    mul()
elif(choice==4):
    div()
else:
    print("invalid")
