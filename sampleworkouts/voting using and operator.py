# Check whether the person is able to vote usin AND operator
age=int(input("Enter your age:"))
if(age>=18 and age<=120):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")