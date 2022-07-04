lst=[]
even_lst=[]
odd_lst=[]
for i in range(1,76):
    lst.append(i)
print(lst)
for i in lst:
    if(i%2==0):
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(even_lst)
print(odd_lst)
print(sum(lst))
print(sum(even_lst))
print(sum(odd_lst))