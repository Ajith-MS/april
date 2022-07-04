#1.create a list from element of a range from 1200-2000 with steps of 130
lst=[i for i in range(1200,2000,130)]
print(lst)

#2.lst=[44,54,64,74,104] --->lst1=[50,60,70,80,110]
lst1=[44,54,64,74,104]
lst2=[i+6 for i in lst1]
print(lst2)

#3.1-50 [elements sqr >50]
lst3=[i for i in range(1,16) if i**2>50]
print(lst3)

#4.weight above 2000 print name  name should be in uppercase
dic={"sedan":1500,"suv":2000,"pickup":2500,"minivan":2400,"semi":13600,"bicycle":7}
lst4=[i.upper() for i in dic if dic[i]>2000]
print(lst4)