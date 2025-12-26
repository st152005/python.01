from array import *

a=array('i',[11,33,55])
b=array('i',[77,99])

print("a:",a)
a.extend(b)
print("a:",a)

a[2:4]=array('i',[22,44])

print("a:",a)
print("b:",b)

'''
output:
a: array('i', [11, 33, 55])
a: array('i', [11, 33, 55, 77, 99])
a: array('i', [11, 33, 22, 44, 99])
b: array('i', [77, 99])
'''
