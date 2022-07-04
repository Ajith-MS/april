#Enter a student detail using dictionary
#studentname,age,rollno,college,place,phno,parentname venam
dic={"name":'Ajith',"Age":22,"rollno":180021094113,"college":'Jaibharath arts and science college',
     "place":'varapuzha',"phno":9526155487,"pname":'Suresh ms'}
print(dic)
print(dic["name"],dic["Age"])

for k,v in dic.items():
     print(k,":",v)
#update phno
dic["phno"]=8606577229
print(dic)

#update name to Ajith MS
dic["name"]='Ajith MS'
print(dic)

#update place
dic["place"]='Puthenpally'
print(dic)

#delete pname
del dic["pname"]
print(dic)

#add new key and value
dic["dep"]='BCA'
print(dic)

#