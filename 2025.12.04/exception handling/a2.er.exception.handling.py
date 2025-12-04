'''
Title: Example for without Exception Handling
'''

m1=float(input('Enter Mark-1:'))

m2=float(input('Enter Mark-2:'))

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
Enter Mark-1:fox
Traceback (most recent call last):
  File "D:/stalin/python/app/console/ide.internal/exception handling/a2.er.exception.handling.py", line 5, in <module>
    m1=float(input('Enter Mark-1:'))
ValueError: could not convert string to float: 'fox'
'''
