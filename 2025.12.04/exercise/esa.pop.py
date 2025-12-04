print('Enter following input for develop Empolyee Salary Allowenss ')

eid=input('Empolyee ID:')
ename=input('Empolyee Name:')
sal=input('Salary:')


print(eid,type(eid))
print(ename,type(ename))
print(sal,type(sal))

eid=int(eid)
sal=float(sal)

print(eid,type(eid))
print(ename,type(ename))
print(sal,type(sal))

hra= sal*20/100
da= sal*15/100
pf= sal*35/100
gpay= sal+hra+da
npay=gpay-pf

print('Empolyee ID:',eid)
print('Empolyee Name:',ename)
print('Salary:',sal)
print('House Rent Allowenss:',hra)
print('Dearness Allowenss:',da)
print('provident fund:',pf)
print('Gross Pay:',gpay)
print('Net Pay:',npay)

'''
Enter following input for develop Empolyee Salary Allowenss 
Empolyee ID:1001
Empolyee Name:x5
Salary:100000

1001 <class 'str'>
x5 <class 'str'>
100000 <class 'str'>

1001 <class 'int'>
x5 <class 'str'>
100000.0 <class 'float'>

Empolyee ID: 1001
Empolyee Name: x5
Salary: 100000.0
House Rent Allowenss: 20000.0
Dearness Allowenss: 15000.0
provident fund: 35000.0
Gross Pay: 135000.0
Net Pay: 100000.0
'''
