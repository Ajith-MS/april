#Word count
line=("cat bat rat cat bus bat rat cat rat bat")
data=line.split(' ')
print(data)
dic={}
for i in data:
    if(i in dic):
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
