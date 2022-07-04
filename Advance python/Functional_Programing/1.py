#read a string from console remo
data='apple'
vowels='aeiouAEIOU'
n=""
for i in data:
    if(i not in vowels):
        n+=i
print(n)
