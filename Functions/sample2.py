#syntax for applying another module in this module
#import package_name.module_name
#variable_name=package_name.module_name.fncall

import Functions.sample1
data=Functions.sample1.add(10,20)
print(data)

data1=Functions.sample1.sub(20,10)
print(data1)

data2=Functions.sample1.mul(20,3)
print(data2)

data3=Functions.sample1.div(20,5)
print(data3)
