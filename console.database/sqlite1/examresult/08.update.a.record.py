import sqlite3

con=sqlite3.connect("collegeDBs.db")
cr=con.cursor()
try:
    cr.execute("update ExamResult set M2=34.5 where RNo=1002")
    con.commit()

    print(cr.rowcount,"no.of rows affected")
except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()
    
'''
output:
1 no.of rows affected
'''
