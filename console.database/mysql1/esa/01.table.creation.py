from mysql import connector

cn=connector.connect(host='localhost',port=3306,database='cmrdb',user='root',password='')
cr=cn.cursor()

qry1="""drop table if exists esatbl"""

qry2="""
create table if not exists esatbl
(
eid int primary key auto_increment,
ename varchar(5) not null,
sal decimal(11,2) unsigned default 0,
hra decimal(11,2) as (sal*20.0/100),
da decimal(11,2) as (sal*15.0/100),
pf decimal(11,2) as (sal*35.0/100),
gpay decimal(11,2) as (sal+hra+da),
npay decimal(11,2) as (gpay-pf)
)auto_increment=1001;
"""
try:
    cr.execute(qry1)
    print("\nErased 'esatbl' table")
except Exception as e:
    print("\nError.:",e)

try:
    cr.execute(qry2)
    print("\nCreate 'esatbl' table")
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

Erased 'esatbl' table

Create 'esatbl' table

Disconnect MySQL
'''

