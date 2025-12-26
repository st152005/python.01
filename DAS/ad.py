from array import *

L=[11,33,77]

a=array('i',L)
print(a)

print(a[2])
a[2]=55
print(a[2])

print(a)
a.append(77)
print(a)

a.append(55)
print(a)

a.remove(55)
print(a)

a.remove(55)
print(a)

try:
    a.remove(55)
except Exception as e:
    print("Err.:",e)

'''
output:
array('i', [11, 33, 77])
77
55
array('i', [11, 33, 55])
array('i', [11, 33, 55, 77])
array('i', [11, 33, 55, 77, 55])
array('i', [11, 33, 77, 55])
array('i', [11, 33, 77])
Err.: array.remove(x): x not in array
'''









    


