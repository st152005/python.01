import sqlite3

con=sqlite3.connect("collegeDBs.db")

try:
    query="""
create trigger ExamResult_TrgIns after insert on ExamResult
Begin
     update ExamResult set Total=(new.M1 + new.M2), Average=(new.M1 + new.M2) / 2 where RNo=new.RNo;
     update ExamResult set Result='Fail' where RNo=new.RNo;
     update ExamResult set Result='Pass' where (new.M1 > 34.4 and new.M2 > 34.4) and RNo=new.Rno;
End;
"""

    con.execute(query)
    con.commit()

    print("Successfully create before insert trigger")
except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()

'''
output:
Successfully create before insert trigger
(or)
Err.:  trigger ExamResult_TrgIns already exists
'''
