#Reverse  153     351
num=int(input("Enter a Number :"))
res=0
while(num!=0):
    dig=num%10              #dig=153%10=3       dig=15%10=5         dig=1%10=1
    res=(res*10)+dig        #res=0*10+3=3       res=(3*10)+5        res=(35*10)+1
    num=num//10             #num=153//10=15     num=15//10=1        num=1//10=0
print(res)                  #3                  35                  351