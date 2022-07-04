dic={"roll":101,"name":'vinay',"age":26,"dep":'bigdata',"marks":30}
# dic2={"roll":102,"name":'ajith',"age":24,"dep":'python',"marks":60}
print(dic)
# print(dic2)
# print(dic["marks"])
# print(dic["name"])
#
# #update value in dictonary
# #marks 30-->40
# dic["marks"]=40     or       dic["marks"]+=10
# print(dic)
#
# dic2["marks"]=80
# print(dic2)
#
# #update bigdata --> python,python-->bigdata
# dic["dep"]='python'
# dic2["dep"]='bigdata'
# print(dic)
# print(dic2)
for i in dic:
    print(i,",",dic[i])

#to add new key and value to a dictonary
dic["total"]=150
print(dic)

#to delete a key and value
del dic["roll"]
print(dic)

#statement true or false
print("name" in dic)
print("name" not in dic)


