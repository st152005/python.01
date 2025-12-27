import sqlite3

con=sqlite3.connect("collegeDBs.db")

try:
    query="""
create trigger ExamResult_TrgUpd after update on ExamResult
Begin
    update ExamResult set Total=(new.M1 + new.M2),Average=(new.M1 + new.M2)/2 where RNo=new.Rno;
    update Examresult set Result='Fail' where RNo=new.RNo;
    update Examresult set Result='Pass' where (new.M1 > 34.4 and new.M2 >34.4) and RNo=new.RNo;
End;
"""

    con.execute(query)
    con.commit()

    print("Successfully create before update trigger")
except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()

'''
output:
Successfully create before update trigger
(or)
Err.:  trigger ExamResult_TrgUpd already exists
'''
