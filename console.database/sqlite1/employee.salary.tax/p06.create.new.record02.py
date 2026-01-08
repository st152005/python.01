import sqlite3
ename=(input("Enter Employee Name: "))
sal=int(input("Enter Employee Salary: "))

con=sqlite3.connect("tsdb.db")
cr=con.cursor()
try:
    query="insert into tblest (ename,sal)values('%s','%5.2f')"%(ename,sal)
    cr.execute(query)
    con.commit()
    print(cr.rowcount, "no. of rows affected")

except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()

'''
output:
Enter Employee Name: x5
Enter Employee Salary: 1200000
1 no. of rows affected
'''
