from mysql import connector

cn=connector.connect(host='localhost',port=3306,database='cmrdb',user='root',password='')
cr=cn.cursor()

qry1="""insert into esatbl(ename,sal)values('x5',500000)"""

qry2="""
insert into esatbl
(ename,sal)
values
('x3',300000),
('x1',100000),
('x2',200000),
('x4',400000)
"""
try:
    cr.execute(qry1)
    print("\nOne row affected")
except Exception as e:
    print("\nError.:",e)

try:
    cr.execute(qry2)
    cn.commit()
    print("\nAffected rows:",cr.rowcount)
except Exception as e:
    print("\nError.:",e)
    

try:
    cr.close()
    cn.close()
    print("\nDisconnect MySQL")
except Exception as e:
    print("\nErro.:",e)


'''
output:

One row affected

Affected rows: 4

Disconnect MySQL
'''
