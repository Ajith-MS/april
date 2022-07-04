#
import re
s="abcaaaaaaaaaaaabcccccccabcaaaaaaaaaaaaaabcbbbbbbbbbbbbabc"
mat=re.finditer('abc',s)
print(mat)
count=0
for i in mat:
    count+=1
    print(i.group())
    print(i.start())
print(count)
