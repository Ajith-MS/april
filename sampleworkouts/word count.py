file=open("wrd cnt file","r")
dic={}
for i in file:
    data=i.rstrip("\n").split(' ')
    print(data)
    for i in data:
        if(i not in dic):
            dic[i]=1
        else:
            dic[i]+=1
for k,v in dic.items():
    print(k,":",v)