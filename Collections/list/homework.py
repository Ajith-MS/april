#read number from the list
#print pair of numbers
#eg:- 6>>  (4,2),(2,4),(3,3)
lst=[4,3,2,1]
num=int(input("Enter the number :"))
flag=0
for i in lst:
    for j in lst:
        if(num==i+j):
            print("(",i,j,")")
            flag=1
if(flag>0):

