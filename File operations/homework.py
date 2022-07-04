f=open("D:/Dont delete windows files/Downloads/temperature","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(',')
    print(data)
    dist=data[0]
    temp=data[1]
        if dist not in dic:
            dic[dist]=temp
        else:
            old_temp=dic[dist]
            if(old_temp>temp):
                dic[dist]=temp
print(dic)
