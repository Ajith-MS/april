# check whether the person is male or female using OR operator
gender=input("Are you a Male (y/n):")
if(gender=='y' or gender=='Y'):
    print("You are Male.")
elif(gender=='n' or gender=='N'):
    print("You are Female.")
else:
    print("invalid charater!")