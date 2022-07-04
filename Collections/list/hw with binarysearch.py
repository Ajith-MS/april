lst=[4,3,2,1]
lst.sort()
print(lst)
num=int(input("Enter the number :"))
low=0
upp=len(lst)-1
while(low<=upp):
    data=lst[low]+lst[upp]
    if(num==data):
        print("Pairs are :",lst[low],lst[upp])
        break
        elif()
