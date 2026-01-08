import sqlite3
con=sqlite3.connect("tsdb.db")
cr=con.cursor()
try:
    query="update tblest set sal=1400000 where eid=1004"
    cr.execute(query)
    con.commit()

    print(cr.rowcount,"no. of rows affected")
except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()

'''
output:
1 no. of rows affected
'''
