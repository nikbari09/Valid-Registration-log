from sqlconnection import *
dbCursor =myDB.cursor()
dbCursor.execute("CREATE TABLE students(no int(11) AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), email VARCHAR(255), age int(11), password VARCHAR(25))")
print("TABLE IS CREATED!")


