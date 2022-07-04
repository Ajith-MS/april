f=open("word_count_file","r")
special="!@#$%^&*()[]{}<>,\/|?"
for i in f:
    data=i.rstrip("\n").split(' ')
    str1=""
    for j in data:
        if j not in special:
            str1+=j
    print(str1)

