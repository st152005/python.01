import sqlite3
con=sqlite3.connect("tsdb.db")
print("Successfully created or open database")
con.close()

'''
output:

Successfully created or open database

'''
