#
sub1=int(input("Enter the mark of Your 1st Subject :"))
sub2=int(input("Enter the mark of Your 2nd Subject :"))
sub3=int(input("Enter the mark of Your 3rd Subject :"))
sub4=int(input("Enter the mark of Your 4th Subject :"))
total=sub1+sub2+sub3+sub4
print(total)
if(total>180):
    print("Grade= A+")
elif(total>=160)&(total<=179):  #or we can use elif(160<=total<=179)
    print("Grade= A")
elif(total>=140)&(total<=159):  #or we can use elif(140<=total<=159)
    print("Grade= B+")
elif(total>=120)&(total<=139):  #or we can use elif(120<=total<=139)
    print("Grade= B")
elif(total>=100)&(total<=119):  #or we can use elif(100<=total<=119)
    print("Grade= C+")
elif(total>=80)&(total<=99):    #or we can use elif(80<=total<=99)
    print("Grade= c")
else:
    print("you failed")