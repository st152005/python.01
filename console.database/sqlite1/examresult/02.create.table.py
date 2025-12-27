import sqlite3

con = sqlite3.connect("collegeDBs.db")

try:
    query="""
create table 'ExamResult'
(
 'RNo' integer not null primary key autoincrement,
 'SName' text not null,
 'M1' numeric check(M1 >= 0 and M1 <= 100),
 'M2' numeric check(M2 >= 0 and M2 <= 100),
 'Total' numeric ,
 'Average' numeric,
 'Result' text not null default 'Fail' check(Result == 'Pass' or Result == 'Fail')
);
"""

    con.execute(query)
    con.commit()

    print("Successfully create new table")

except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()

'''
output:
Successfully create new table

(or)

Err.:  table 'examresult' already exists

'''
