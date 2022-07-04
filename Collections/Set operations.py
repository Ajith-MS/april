#Set operations

#1.Union
#combination of two sets
st1={1,2,3,4,5,6,7,8,9,10}
st2={7,8,9,10,11,12,13,14,15}
#syntax:-
st3=st1.union(st2)
print(st3)

#2.Intersection
#to collect common elements from two sets
#syntax:-
st3=st1.intersection(st2)
print(st3)

#3.Difference
#a-b
#elements present in set a but not present in set b
st3=st1.difference(st2)
print(st3)
st3=st2.difference(st1)
print(st3)
