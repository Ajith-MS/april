pattern='ABCDBCDEF'
#first recursive character
dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print(i,"is the first recursive character")
        break

