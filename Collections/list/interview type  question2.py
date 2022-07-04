lst=[4,5,10,12,20]
#lst1=[47,46,41,39,31]
#[51]  [51-4   51-5   51-10   51-12   51-20]
lst1=[]
for i in lst:
    res=sum(lst)-i
    lst1.append(res)
print(lst1)

