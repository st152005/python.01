from umath.computation.ucalculator import *

obj=UCalc()

print(obj.usum())
obj.uproduct()

obj.readInt()

print(obj.usum())
obj.uproduct()

obj.readFloat()

print(obj.usum())
obj.uproduct()

del obj

'''
output:

Default Constructor
0
0
Enter x value:2
Enter y value:7
9
14
Enter x value:0.2
Enter y value:5
5.2
1.0

Destructor processing...

'''
