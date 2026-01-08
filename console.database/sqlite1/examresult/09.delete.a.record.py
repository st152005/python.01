import sqlite3

con=sqlite3.connect("collegeDBs.db")

vName='Greaps'

try:
    con.execute("Delete from ExamResult where SName='%s'"%(vName))
    con.commit()

    print(con.total_changes,"no.of rows affected")
except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()

'''
output:
1 no.of rows affected
'''
