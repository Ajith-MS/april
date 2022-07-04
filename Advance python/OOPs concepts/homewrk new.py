#find highest mark print fname
lst=[('vinay',45),('arjun',35),('amal',65),('vipin',56)]
marks=[]
for i in lst:
    marks.append(i[1])
#print(marks)
maximum=max(marks)
for j in lst:
    if(j[1]==maximum):
        print(j[0])
