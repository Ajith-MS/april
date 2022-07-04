#
#lst=[7,4,3,1,2]
#1.sort the given list in ascending order  lst=[1,2,3,4,7]
#2.declare 2 variable   low,  upp
#low=0
#upp=len(lst)-1       upp=4
#3.calculate mid  mid=(low+upp)//2    mid=2
#4.check 3 condition
#   1.  search_element>lst[mid]         #lst[2]    4>3
#        low=mid+1
#   2.  search_element<lst[mid]         #lst[2]    2<3
#        upp=mid-1
#   3.   search_element==lst[mid]       #3==3        element found
#
lst=[1,4,5,8,2,3,9,10,7,6]
lst.sort()
print(lst)
num=int(input("Enter a number you want to be searched for :"))
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