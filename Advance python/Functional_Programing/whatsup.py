#1. Find all of the numbers from 1-1000 that are divisible by 7
lst=[i for i in range(1,1001) if i%7==0]
print(lst)

#2. Find all of the numbers from 1-1000that have a 3 in them
lst1=[i for i in range(1,1001) if '3' in str(i)]
print(lst1)

#3.count the number of space in a string create a list of all the consonants in the string
data='Yellow Yaks like yelling and yawning and yesturday the yodled while eating yuky yams'
lst2=[i for i in data if i==' ']
print(len(lst2))
