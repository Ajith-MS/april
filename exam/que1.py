#  check whetheer the given string is palindrome or not ?
s1=input("Enter the string to check Palindrome :")
s2=" "
for i in s1:
    s2=i+s1
print(s2)
if(s1==s2):
    print("it is palindrome")
else:
    print("it is not palindrome")