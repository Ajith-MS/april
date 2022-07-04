# Avoid duplicates and add values to the new list
lst=[10,10,20,20,30,30,40,40,50,50,60,60,70,70,80,80,90,100]
lst1=[]
print(lst)
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)