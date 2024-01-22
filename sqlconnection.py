import mysql.connector

myDB=mysql.connector.connect(
    host="localhost",
    user="Nikhil",
    password="",
    database="Registration"
)

print("Database connected",myDB)

'''dbCursor =myDB.cursor()
dbCursor.execute("CREATE DATABASE Registration")
print("Database Created")'''
'''dbCursor.execute("SHOW DATABASES")
for i in dbCursor:
    print(i)'''



