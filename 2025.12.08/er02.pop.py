'''
Title: How to develop exam result
'''

m1=float(input('Enter Mark-1:'))
m2=float(input('Enter Mark-2:'))

result='Pass' if m1>34.4 and m2>34.4 else 'Fail'

print('Mark-1: %2f' %(m1))
print('Mark-2: %2f' %(m2))
print('Result: %s'%(result))

'''
Output-01:
Enter Mark-1:56.5
Enter Mark-2:63
Mark-1: 56.500000
Mark-2: 63.000000
Result: Pass

Output-02:
Enter Mark-1:80
Enter Mark-2:20
Mark-1: 80.000000
Mark-2: 20.000000
Result: Fail

'''
