'''
Title: How to develop Employee Salary Tax 
'''

print('Enter following input for develop Employee Salary Tax')

eid=int(input('Enter Employee ID: '))
ename=input('Enter Employee Name: ')
sal=float(input('Salary: '))

tax10=tax20=tax30=0

if sal>1000000:
    tax10=25000
    tax20=100000
    tax30=(sal-1000000)*30/100

elif sal>500000:
    tax10=25000
    tax20=(sal-500000)*20/100
    tax30=0

elif sal>250000:
    tax10=(sal-250000)*10/100
    tax20=0
    tax30=0

tottax= tax10 + tax20 + tax30
np=sal-tottax


print('Empolyee ID:',eid)
print('Empolyee Name: ',ename)
print('Salary:',sal)
print('Total Tax:',tottax)
print('Net Pay:',np)


'''
Output:

Enter following input for develop Employee Salary Tax
Enter Employee ID: 1001
Enter Employee Name: x5
Salary: 1000000

Empolyee ID: 1001
Empolyee Name:  x5
Salary 1000000.0
Total Tax 350000.0
Net Pay 650000.0

'''
