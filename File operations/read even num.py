f=open("numbers","r")
lst=[]
even_sum=[]
odd_sum=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
for i in lst:
    if(i%2==0):
        even_sum.append(i)
    else:
        odd_sum.append(i)
print(even_sum)
print(odd_sum)
print("Sum of evem numbers =",sum(even_sum))
print("Sum of odd numbers =",sum(odd_sum))
