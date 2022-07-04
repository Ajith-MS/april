# Python program to print prime number between 0 to 100
count=0
for i in range(0,101):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            count+=1
            print(i)
print("count =",count)