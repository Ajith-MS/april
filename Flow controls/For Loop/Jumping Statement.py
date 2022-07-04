# JUMPING STATEMENTS
#break
#continue
#pass


#Break statement  :-
for i in range(1,51):
    if(i==25):
        break
    print(i)


#Continue statement :- skip number 25 and print 1-50
for i in range(1,51):
    if(i==25):
        continue
    print(i)

#Pass statement  :- do nothing
for in range(1,51):
    if(i==25):
        pass
    print(i)
# eg 1-50 even number-do nothing,odd number-print sguare
for i in range(1,51):
    if(i%2==0):
        pass
    else:
        print(i**2)
