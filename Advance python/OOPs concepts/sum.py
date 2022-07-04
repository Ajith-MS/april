#
# def Sum(*args):
#     print(sum(args))
# Sum(1,2,3,4,5,6,7,8)


#method2
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum