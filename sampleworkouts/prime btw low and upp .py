low=int(input("Enter the Lowerlimit :"))
upp=int(input("Enter the Upperlimit :"))
flag=0
for i in range(low,upp):
    if(i>1):
        for j in range(2,upp):
            if(i%j==0):
                break
        else:
            print(i)

