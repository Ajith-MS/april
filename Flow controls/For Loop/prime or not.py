#check whether given number is prime or not
#Eg: 2,3,5,7,11,........
#9 prime aanonn check cheyyan (2,8) 2 muthal 8 vare eethenkilum oru no. ne kond divede cheyyan pattunnundonn nokkanam

num=int(input("Enter a Number :"))
flag=0
for i in range(2,num):              
    if(num%i==0):
       flag=1
       break
if(flag>0):
    print(num," is not a Prime number")
else:
    print(num," is a Prime number")

