from array import *

t=(11,33,55,77,99)

a=array('i',t)

for e in a:
    print(e)

a[2]=66

print(a)

'''
output:
11
33
55
77
99

array('i', [11, 33, 66, 77, 99])
'''
