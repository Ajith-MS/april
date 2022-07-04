#1 1 1 1 1
#2 2 2 2 2
#3 3 3 3 3
#4 4 4 4 4
#5 5 5 5 5
for i in range(1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()
print()

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
for i in range(1,6):
    for j in range(1,6):
        print(j,end=' ')
    print()
print()

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()

#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
print()

#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5
for i in range(1,6):
    for j in range(i,6):
        print(i,end=' ')
    print()
print()

#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()
print()

#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1
for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=' ')
    print()
print()

#1 2 3 4 5
#2 3 4 5
#3 4 5
#4 5
#5
for i in range(1,6):
    for j in range(i,6):
        print(j,end=' ')
    print()
print()

#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
print()

#0 1 2 3 4 5
#0 1 2 3 4
#0 1 2 3
#0 1 2
#0 1
for i in range(1,6):
    for j in range(0,6,-1):
        print(j,end=' ')
    print()

