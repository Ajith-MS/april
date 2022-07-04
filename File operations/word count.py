#
dic={}
f=open("new","r")
for i in f:
    data=i.rstrip("\n").split(' ')
    print(data)
    for i in data:
        if(i not in dic):
           dic[i]=1
        else:
            dic[i]+=1
print(dic)
for i in dic:
    print(i,",",dic[i])

#or another method of iterating of key value pairs
for k,v in dic.items():
    print(k,":",v)