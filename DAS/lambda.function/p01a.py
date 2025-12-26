'''
Title:Example for Lambda function(reduce)
'''

from functools import reduce

def add(i,j):
    return i+j

L1=[1,3,5,7,9]
L2=reduce(add,L1)

print(L1)
print(L2)

'''
output:
[1, 3, 5, 7, 9]
25
'''
