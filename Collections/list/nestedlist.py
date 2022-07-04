#Nested list
#oru list il thanne multiple list form cheyyan pattum

lst=[[101,'arun','k',26,'bigdata',1000],
     [102,'amal','p',27,'python',1500],
     [103,'vishnu','e',24,'bigdata',1250],
     [104,'anoop','m',27,'python',2000],
     [105,'hari','r',25,'bigdata',1750],
     [106,'vinay','s',28,'bigdata',1500]]
#print(lst)
#print lst line by line
for i in lst:
     print(i)
#print fname,lname,age,profession
for i in lst:
     print(i[1],i[2],i[3],i[4])
# or
for i in lst:
     print(i[1:5])
print()

#age above 25  fname,lname,age,proff,salary
for i in lst:
     if(i[3]>25):
          print(i[1],i[2],i[3],i[4],i[5])
print()

#proff big data ,  fname,lname,age,salary
for i in lst:
     if(i[4]=='bigdata'):
          print(i[1],i[2],i[3],i[5])
print()

#salary above
for i in lst:
     if((i[5]>1750)&(i[3]>25)):
          print(i[1],i[2],i[3],i[4],i[5])
print()

#total salary
sum=0
for i in lst:
     sum+=i[5]
print("sum of salary=",sum)