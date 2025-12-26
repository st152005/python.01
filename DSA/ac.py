from array import *

L=[1001,'x5',56.5,63]

try:
    a=array('d',L)
    print(a)
except Exception as e:
    print("Err.:",e)

try:
    a=array('u',L)
    print(a)
except Exception as e:
    print("Err.:",e)

'''
output:
Err.: must be real number, not str

Err.: array item must be unicode character

'''
