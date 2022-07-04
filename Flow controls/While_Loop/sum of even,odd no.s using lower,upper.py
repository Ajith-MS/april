# Read the lower limit and upper limit from the console and print even nos. sum  and odd no.s sum.
low=int(input("Enter the lower limit :"))
upp=int(input("Enter the upper limit :"))
sum=0
summ=0
while(low<=upp):
    if(low%2==0):
        sum+=low
    else:
        summ+=low
    low+=1
print("Sum of EVEN numbers =",sum)
print("Sum of ODD numbers  =",summ)