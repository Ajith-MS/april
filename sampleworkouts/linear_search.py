lst=[1,2,3,4,5,6,7,8,9,10]
num=int(input("Enter a number you want to search for :"))
flag=0
for i in lst:
    if(num==i):
        flag=1
        break
if(flag>0):
    print("Element found")
else:
    print("Element not found")

