import re
s='[love123]'
find=re.finditer(s,'alslovealslovealslovealslovealsloveals123123')
print(find)
count=0
for i in find:
    count+=1
    print(i.group())
    print(i.start())
