# to reduce length of code

#lambda
#map
#filter
#reduce
#list-comprehension

#1. lambda function
#it has no identity(anonymous function aan)
#variable name=lambda arguments:operation
#syntax:-
f=lambda num1,num2:num1+num2
print("sum of numbers=",f(20,30))

#to multiply 3 numbers using lambda function
f=lambda num1,num2,num3:num1*num2*num3
print("Product of 3 numbers=",f(10,20,30))

#find cube of a number
f=lambda num:num**3
print("cube of a number=",f(10))


#2,3. map, filter
#map:-oru listil  ella elements corresponding output create cheyyanam
#filter:-oru listil olla elements condition vech output create cheyyanam
#syntax:-
#variable_name=list(map(argument1,argument2))
#variable_name=list(filter(argument1,argument2))
#argument1==>function
#argument2==>iterable
#eg
lst=[1,2,3,4,5,6,7,8,9,10]
#map
# def square(num):
#     res=num**2          lambda num:num**2
#     return res
#data=list(map(square,lst))
data=list(map(lambda num:num**2,lst))
print(data)

#filter
#data=list(filter)


#list-comprehension
# lst1=[]
# for i in range(1,101):
#     lst1.append(i)
# print(lst1)
#syntax:-lst=[print range]
lst1=[i for i in range(1,101)]
print(lst1)


#1,..75(1,5,9,13,17,21...)
lst2=[i for i in range(1,76,4)]
print(lst2)


#1 to 100 even numbers
#syntax:-  lst=[print range condition]
lst3=[i for i in range(1,101) if i%2==0]
print(lst3)

#more than one condition occur:
#syntax:-
#[print if condition else print range]

#[print1 if condition1 else print2 if condition2 else print range]

#[print1 if condition1 else print2 else if condition2 else print3 if condition3 else print range]
