low=int(input("Enter the lower limit :"))
upp=int(input("Enter the upper limit :"))
even_sum=0
odd_sum=0
for i in range(low,upp+1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print("Sum of even numbers =",even_sum)
print("Sum of odd numbers =",odd_sum)