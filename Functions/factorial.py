#Factorial
def factorial():
    num=int(input("Enter a number :"))
    mul=1
    for i in range(1,num+1):
        mul*=i
    print(mul)
factorial()

def fact(num):
    mult=1
    for i in range(1,num+1):
        mult*=i
    print(mult)
fact(3)

def fac(num):
    multi=1
    for i in range(1,num+1):
        multi*=i
    return multi
data=fac(3)
print(data)