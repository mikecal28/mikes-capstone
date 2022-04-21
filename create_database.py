import sqlite3


connection = sqlite3.connect('capstone_database.db')
cursor = connection.cursor()

with open("tables.sql") as sql_file:
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
       

print("Database Created Successfully!")