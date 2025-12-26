'''
Title:Example for Lambda function(reduce) using Lambda expression
'''

from functools import reduce

mul=lambda x,y:x*y

L1=[2,4,6,8,1]
L2=reduce(mul,L1)

print(L1)
print(L2)

'''
output:
[2, 4, 6, 8, 1]
384
'''
