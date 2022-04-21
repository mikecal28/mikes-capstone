import sqlite3
from pprint import pprint

connection = sqlite3.connect("capstone_database.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


# users_dict = {}
# competencies_dict = {}
# for users_row in cursor.execute("SELECT * FROM Users"):
#     users_dict[users_row[1]] = users_row

# for competencies_row in cursor.execute("SELECT * FROM Competencies"):
#     competencies_dict[competencies_row[1]] = competencies_row
    
# pprint(users_dict)
# print()
# pprint(competencies_dict)



cursor.execute("SELECT * FROM Users")
row = cursor.fetchone()

# print(type(row))
# print(tuple(row))
# print(len(row))
# print(row[2])
print(row.keys())
# print(row['first_name'])

# print(list(row))



# 16
# 3
# 8
# =27

