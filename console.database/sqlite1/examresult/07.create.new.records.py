import sqlite3

con=sqlite3.connect("collegeDBs.db")
cr=con.cursor()
try:
    query="Insert into ExamResult(SName,M1,M2)values('Banana',65.5,56),('Orange',45,54.5)"
    cr.execute(query)
    con.commit()

    print(cr.rowcount,"no.of rows affected")
except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()
    
'''
output:
2 no.of rows affected
'''
