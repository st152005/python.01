import sqlite3
con=sqlite3.connect("tsdb.db")
cr=con.cursor()

try:
    query="""
create table 'tblest'
(
  'eid' integer not null primary key autoincrement,
  'ename' text not null,
  'sal' numeric(10,2),
  'tax10' numeric(8,2),
  'tax20' numeric(8,2),
  'tax30' numeric(8,2),
  'tottax' numeric(8,2),
  'np' numeric(10,2)
  );
"""
    cr.execute(query)
    con.commit()
    print("Successfully created new table")

except Exception as ex:
    con.rollback()
    print("Err.: ",ex)

con.close()
'''
output:
Successfully created new table
'''
\
