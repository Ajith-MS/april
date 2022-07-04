#Exceptional handling
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
try:
    div=num1/num2
    print(div)
# except:
#     print("zero division error")
# finally:
#     print("inside")
except Exception as e:
    print("error",e)

# code ile error alla ,input il kodukkana error aan exceptional handling

#3 blocks
#1.try block:
#exception varan chance ulla code try blockil add cheyyum

#2.except block
#exception vannal ath ath mattan ollan solution  kodukkan olla code aan

#3.finally
#prethyekich upakaram onnula error indenkilum illenkilum ath wrk cheyyum

#How to identify an exception case:
# a=[1,2,3,4]
# i=int(input("Enter a index"))
# try:
#     print(a[i])
# except Exception as e:
#     print("error !",e)


#How to generate Exception
