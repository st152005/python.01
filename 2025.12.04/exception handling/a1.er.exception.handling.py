'''
Title:Example for Exception Handling
'''
m1=m2=0

try:
    m1=float(input('Enter Mark-1:'))
except Exception as e:
    print('Error:',e)
    m1=0

try:
    m2=float(input('Enter Mark-2:'))
except Exception as e:
    print('Error:',e)
    m2=0

print(f'Mark-1:{m1}\nMark-2:{m2}\nTotal:{m1+m2}')

'''
input-01:
Enter Mark-1:56.5
Enter Mark-2:63

output-01:
Mark-1:56.5
Mark-2:63.0
Total:119.5

input-02:
Enter Mark-1:orange
Error: could not convert string to float: 'orange'
Enter Mark-2:63

output-02:
Mark-1:0
Mark-2:63.0
Total:63.0

input-03:
Enter Mark-1:fox
Error: could not convert string to float: 'fox'
Enter Mark-2:1.2.3.4.5
Error: could not convert string to float: '1.2.3.4.5'

output-03:
Mark-1:0
Mark-2:0
Total:0
'''
