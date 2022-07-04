#Word count of the file word_count_file
f=open("word_count_file","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(" ")
    print(data)
    for i in data:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
for k,v in dic.items():
    print(k,":",v)