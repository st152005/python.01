from array import *

L=[1,3,5,7,9]

a=array('d',L)
print(a,"\n",a.typecode,sep='')

a=array('f',L)
print(a,"\n",a.typecode,sep='')

a=array('i',L)
print(a,"\n",a.typecode,sep='')

'''
output:
array('d', [1.0, 3.0, 5.0, 7.0, 9.0])
d
array('f', [1.0, 3.0, 5.0, 7.0, 9.0])
f
array('i', [1, 3, 5, 7, 9])
i
'''
