#Basic rules for Regular expression
import re
count=0
#rule='[abc]'                              #rule1:square brackets il ittal ath etra pravisham indenn
#rule='[^abc]'                             #rule2:^ koduthal abc ozhike olla baki ellam varum
#rule='[A-Z]'                               #rule3:capital A-Z olla ellam print aavum
rule='[^0-9a-zA-Z]'
matcher=re.finditer(rule,'abc @ajith')
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print("total count=",count)

#hacker_rank