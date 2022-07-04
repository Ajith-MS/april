lst=[1,6,10,7,4,8,3,2,9,5]
lst.sort()
print(lst)
num=int(input("Enter the element to be searched for :"))
low=0
upp=len(lst)-1
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upp=mid-1
    elif(num==lst[mid]):
        flag=1
        break
if(flag>0):
    print("Element found")
else:
    print("Element not found")

