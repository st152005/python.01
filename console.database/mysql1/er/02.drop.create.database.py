from mysql import connector

cn=connector.connect(host='127.0.0.1',port=3306,database='',user='root',password='')
cr=cn.cursor()

try:
    cr.execute("""drop database if exists cmrdb""")
    cr.execute("""create database if not exists cmrdb""")
    print('\nCreated new database')
except Exception as e:
    print('Error.:',e)

try:
    cr.close()
    cn.close()
    print("\nDisconnect MySQL")
except Exception as e:
    print("\nErro.:",e)
'''
output:
Created new database

Disconnect MySQL

'''
    
