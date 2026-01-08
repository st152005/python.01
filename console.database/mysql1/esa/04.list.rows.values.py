from mysql import connector

cn=connector.connect(host='127.0.0.1',port=3306,database='cmrdb',user='root',password='')
cr=cn.cursor()

qry="""select * from esatbl"""

try:
    cr.execute(qry)
    rows=cr.fetchall()
    print('No.of columns:',len(rows[0]))
    print('No.of rows:',len(rows[1]))
    print('\nFollowing rows values...\n')

    for row in rows:
        print()
        for col in row:
            print(f'{col:<{10}}',end='')
except Exception as e:
    print('\nError.:',e)

try:
    cr.close()
    cn.close()
    print('\nDisconnect MySQL')
except Exception as e:
    print('\nError.:')

'''
output:
No.of columns: 8
No.of rows: 8

Following rows values...


1001      x5        700000.00 140000.00 105000.00 245000.00 945000.00 700000.00 
1002      x3        400000.00 80000.00  60000.00  140000.00 540000.00 400000.00 
1003      x1        200000.00 40000.00  30000.00  70000.00  270000.00 200000.00 
1004      x2        300000.00 60000.00  45000.00  105000.00 405000.00 300000.00 
1005      x4        500000.00 100000.00 75000.00  175000.00 675000.00 500000.00 
Disconnect MySQL
'''
