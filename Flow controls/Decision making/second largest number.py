# read 3 numbers from console ,num1,num2,num3 find second largest number
num1=int(input("Enter Number1 :"))
num2=int(input("Enter number2 :"))
num3=int(input("Enter number3 :"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("Second largest number is",num2)
    else:
        print("Second largest number is",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("Second largest number is",num1)
    else:
        print("Second largest number id",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("Second largest number is",num1)
    else:
        print("Second largest number is",num2)
else:
    print("invalid")