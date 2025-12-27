import sqlite3

con = sqlite3.connect("collegeDBs.db")

print("Successfully created or opened database")

con.close()

'''
output:
Successfully created or opened database
'''
