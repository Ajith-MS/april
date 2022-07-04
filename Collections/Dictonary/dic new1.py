#{'vinay':{"designation":'bigdata',"salary":1000},'anu'{"designation":'bigdata',"salary":1000}}
employee=['vinay','anu']
default={"designation":'bigdata',"salary":1000}

#fromkeys :it returns a dictionary with specified keys and specified values
res=dict.fromkeys(employee,default)
print(res)

for k,v in res.items():
    print(k,v)

print(res['vinay'])