#open file form pc
f=open("D:/Dont delete windows files/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    prof = data[4]

    #print(data)
    #print(data[1],",",data[2],",",data[3])
    #print(data[0:4:2])
    #age above 60 fname,lname,age,proff

    # if(data[3]>'60'):
    #     print(data[1],",",data[2],",",data[3],",",data[4])

    # #age above 50 location india fname,lname,age,prof
    # if(data[3]>'50' and data[-1]=='india'):
    #     print(data[1],",",data[2],",",data[3],",",data[4])

#     #each prof count
#     if(prof not in dic):
#         dic[prof]=1
#     else:
#         dic[prof]+=1
# for k,v in dic.items():
#     print(k,":",v)

    #each location count
