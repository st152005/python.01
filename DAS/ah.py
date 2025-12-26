from array import *

s='fox'
b=b'fox'

print(s,type(s))
print(b,type(b))

a=array('b',[11,33,55,77,99])
print(a)

print("Address:",a.buffer_info())
print("Address:",a.buffer_info()[0])
print("Length:",a.buffer_info()[1])

print("Raw bytes:",bytearray(a))

'''
output:
fox <class 'str'>
b'fox' <class 'bytes'>
array('b', [11, 33, 55, 77, 99])
Address: (2509985092400, 5)
Address: 2509985092400
Length: 5
Raw bytes: bytearray(b'\x0b!7Mc')
'''
