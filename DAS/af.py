from array import *

try:
    L=['fox','box']
    a=array('u',L)
    print(a)
except Exception as e:
    print("Err.:",e)


try:
    L=['fox','box']
    a=array('u','fox','box')
    print(a)
except Exception as e:
    print("Err.:",e)

a=array('u','fox')
print(a)

for c in a: print(c)

'''
output:
array('u', 'fox')
f
o
x
'''
