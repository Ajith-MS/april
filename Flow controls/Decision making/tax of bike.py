
costprice=int(input("Cost price of Bike :"))
tax=0
if(costprice>100000):
    tax=(15/100)*costprice
    print("The tax you want to give=",tax)
elif(costprice>50000&costprice<=100000):
        tax=(10/100)*costprice
        print("The tax you want to give=",tax)
elif(costprice<=50000):
    tax=(5/100)*costprice
    print("The tax you want to give=",tax)
else:
    print("Not able to find")