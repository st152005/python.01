print('Enter following input for develop Exam Result exercise...')

rno=input('Roll no:')
sname=input('Student Name:')
m1=input('Mark-1:')
m2=input('Mark-2:')

print(rno,type(rno))
print(sname,type(sname))
print(m1,type(m1))
print(m2,type(m2))


rno=int(rno)
m1=float(m1)
m2=float(m2)


print(rno,type(rno))
print(m1,type(m1))
print(m2,type(m2))

total=m1+m2
avg=total/2

if m1>34.4 and m2>34.4:
    result='Pass'
else:
    result='Fail'

print('Roll no:',rno)
print('Student Name:',sname)
print('Mark-1:',m1)
print('Mark-2:',m2)
print('Total:',total)
print('Average:',avg)
print('Result:',result)

'''
output-01:

Enter following input for develop Exam Result exercise...
Roll no:1001
Student Name:x5
Mark-1:56.5
Mark-2:63

1001 <class 'str'>
x5 <class 'str'>
56.5 <class 'str'>
63 <class 'str'>

1001 <class 'int'>
56.5 <class 'float'>
63.0 <class 'float'>

Roll no: 1001
Student Name: x5
Mark-1: 56.5
Mark-2: 63.0
Total: 119.5
Average: 59.75
Result: Pass

output-02:

Enter following input for develop Exam Result exercise...
Roll no:1002
Student Name:x4
Mark-1:80
Mark-2:32

1002 <class 'str'>
x4 <class 'str'>
80 <class 'str'>
32 <class 'str'>

1002 <class 'int'>
80.0 <class 'float'>
32.0 <class 'float'>

Roll no: 1002
Student Name: x4
Mark-1: 80.0
Mark-2: 32.0
Total: 112.0
Average: 56.0
Result: Fail
'''





