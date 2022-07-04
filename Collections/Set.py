#Set
#set can be defined by '{}' symbol  if the curly brackets is empty it will read as a dictonary so we can use 'set()'
#if the values are in the curly brackets then it will read as set

#1.How to define
st=set()

#2.hetrogeneous data support or not
st1={10,10.5,'bigdata',True,'python'}
print(st1)

#3.insertion order is not preserved
st2={1,20,39,5,'bigdata'}# insertion order is not preserved
print(st2)

#4.duplication is allowed or not
str3={1,2,3,4,5,1,5}#duplication is not allowded
print(str3)

#5.mutable or not
#set is mutable