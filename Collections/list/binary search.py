# Binary search
#list sort cheyyanam
#low value high value assign cheyyaanam
#mid value kand pidikkanam (start=0,end=n, mid=(tart+end)/2
#key value lst[mid] nekalum valuthanenki  first half nokanda
#start=mid+1, end=n  mid value pinnem kand pidikkanam

def binary_search(lst,key):
    low=0
    high=len(lst)-1
    mid=0
    while(low<=high):
        mid=(low+high)//2
        if(lst[mid]<key):
            low=mid+1
        elif(lst[mid]>key):
            high=mid-1
        else:
            return mid
    return -1
lst=[4,7,9,12,13,14]
n=7
r=binary_search(lst,n)
if(r==-1):
    print("Not found")
else:
    print("found")
