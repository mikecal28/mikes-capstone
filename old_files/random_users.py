import requests
import sqlite3
from datetime import datetime
from pprint import pprint

def fake_user_data():
    r1 = requests.get("https://randomuser.me/api/?nat=us")
    r1_dict = r1.json()
    r1_results_dict_list = r1_dict["results"]
    r1_fake_user_dict = {}
    for i in range(len(r1_results_dict_list)):
        r1_fake_user_dict.update(r1_results_dict_list[i])
    return r1_fake_user_dict



connection = sqlite3.connect("capstone_database.db")
cursor = connection.cursor()

for i in range(1):
    random_user_info_dict = fake_user_data()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql_insert = "INSERT INTO Users(first_name, last_name, phone, email, password, date_created, hire_date, user_type) VALUES(?,?,?,?,?,?,?,?)"
    insert_values = (random_user_info_dict['name']['first'], random_user_info_dict['name']['last'], random_user_info_dict['phone'],
                     random_user_info_dict['email'], random_user_info_dict['login']['password'], now, now, 'user')
    cursor.execute(sql_insert, insert_values)
    
connection.commit()



# connection = sqlite3.connect("capstone_database.db")
# cursor = connection.cursor()



# for i in range(16):
    

#     sql_insert = "INSERT INTO Competencies(name) VALUES(?)"
#     competency_list = ['Computer Anatomy','Data Types','Variables','Functions','Boolean Logic',
#                     'Conditionals','Loops','Data Structures','Lists','Dictionaries','Working with Files',
#                     'Exception Handling','Quality Assurance (QA)','Object-Oriented Programming','Recursion','Databases']
    
#     current_competency = competency_list[i]

#     cursor.execute(sql_insert, [current_competency])
#     connection.commit()