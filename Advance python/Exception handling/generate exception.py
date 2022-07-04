#How to generate Exception
#
age=int(input("Rnter the age :"))
if(age>=18):
    print("eligible")
else:
    raise Exception("not allowed")