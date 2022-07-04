lst=[]
lst1=[]
lst2=[]
print(lst)
for i in range(1,101):
    lst.append(i)
print(lst)
for i in lst:
    if(i%5==0):
        lst1.append(i)
print(lst1)
print("Sum of multiple of 5 (5-100) :",sum(lst1))
print("Highest element in the list is :",max(lst1))
print("Smallest element in the list is :",min(lst1))
print("Length of the list 1 is :",len(lst1))
print("Length of list is ",len(lst))
lst1.insert(5,110)
print(lst1)
lst1.remove(5)
print(lst1)
lst1.pop(4)
print(lst1)
print("Now the length of list is :",len(lst1))
for i in lst1:
    if(i%10==0):
        lst2.append(i)
print(lst2)
print(sum(lst2))
print(max(lst2))
print(min(lst2))
print(len(lst2))