
#name ,age, prof ,salary
dic={"name":'ajith',"age":23,"prof":'python',"salary":6000}
print(dic)

#name to fname
dic["fname"]=dic["name"]
del dic["name"]
print(dic)

#print prof
print(dic["prof"])

#check company key is present
print("company" in dic)

#add company:'luminar'
dic["company"]='luminar'
print(dic)

#add salary+5000
dic["salary"]+=5000
print(dic)

#print key-value pairs
for k,v in dic.items():
    print(k,":",v)