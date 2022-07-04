#linear search
#drawback
#complexity increase cheyyum,(time consuming aan)
#time consuming aayath kond aan binary search use cheyyane
lst=[1,5,7,8,3,6,2,9,15,20]
# num=int(input("Enter a number :"))
# if num in lst:
#     print("Element found")
# else:
#     print("Element not found")

#or
num1=int(input("Enter a number :"))
flag=0
for i in lst:
    if(i==num1):
        flag=1
        break
if(flag>0):
    print("Element found at position ",lst[i])
else:
    print("Element not found")