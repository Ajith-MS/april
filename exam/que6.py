# program to print the count of even numbers and odd numbers between lowelimit and upperlimit

low=int(input("Enter the Lower limit :"))
upp=int(input("Enter the Upper limit :"))
count=0
res=0
for i in range(low,upp+1):
    if(i%2==0):
        count+=1
    else:
        res+=1
print("Number of Even no.s :",count)
print("Number of Odd no.s :",res)
