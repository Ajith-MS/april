#largest among 3 numbers.
num1=int(input("Enter Number1 :"))   #100
num2=int(input("Enter Number2 :"))   #80
num3=int(input("Enter Number3 :"))   #60
if(num1>num2)&(num1>num3):           #(100>80)&(100>60)
    print(num1,"is the Largest Number")
elif(num2>num1)&(num2>num3):
    print(num2,"is the Largest Number")
else:
    print(num3,"is the Largest Number")