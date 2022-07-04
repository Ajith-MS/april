#Regular expression:- error message vannathine correct cheyyan aan regular expression use cheyyane
#eg:- phone num 10 digit allenki error vannath

#python package
#pattern matching
#string  aan use cheyyane check cheyyan
#Validation

#Regular expression
import re
s="abaabbbbabbbabaaaabab"
#finditer(argument1,argument2)
#argument1:-find_pattern
#argument2:-srting_name

#ab etra pravisham vanninden nokanam
matcher=re.finditer('ab',s)
print(matcher)
count=0
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())            #i.start()  used for which index is the ab found
print("count of ab=",count)