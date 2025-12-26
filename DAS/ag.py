from array import *

a=array('i',[11,-22,33,-44,55,-66,77,-88,99])
print(a[4])

print(a[-4])

print(a[:4])

print(a[4:])

print(a[4:7])

print(a[4:4])

print(a[:])

print(a[-4:-1])

print(a[::2])

print(a[1::2])

'''
output:
55
-66
array('i', [11, -22, 33, -44])
array('i', [55, -66, 77, -88, 99])
array('i', [55, -66, 77])
array('i')
array('i', [11, -22, 33, -44, 55, -66, 77, -88, 99])
array('i', [-66, 77, -88])
array('i', [11, 33, 55, 77, 99])
array('i', [-22, -44, -66, -88])
'''
