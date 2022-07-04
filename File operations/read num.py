f=open("numbers","r")
lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print("sum=",sum(lst))

#rstrip function
#to remove rightside unwanted things
#eg  line= "hello\n"
#print(line.rstrip("\n"))