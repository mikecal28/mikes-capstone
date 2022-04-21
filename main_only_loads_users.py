import shutil
import bcrypt
import sys
from getpass import getpass
import sqlite3
import ascii_art
import time
import singletons
from pprint import pprint
from os import system
connection_for_row_factory = sqlite3.connect("capstone_database.db")
connection_for_row_factory.row_factory = sqlite3.Row
row_factory_cursor = connection_for_row_factory.cursor()
connection = sqlite3.connect("capstone_database.db")
cursor = connection.cursor()
user_privilege = []
current_user_password_unencrypted = []

CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")
CLEAR_MENU = lambda: print("\x1B[3J\x1B[100A\x1B[20B\x1B[s\x1B[J\x1B[u") # \x1B[20;1H
CLEAR_DISPLAY = lambda: print("\x1B[3J\x1B[100A\x1B[s\x1B[17B\x1B[129C\x1B[1J\x1B[u") # \x1B[17;129H
def MOVE_TO_INPUT():
    print("\x1B[3J\x1B[100A\x1B[26B\x1B[J", end='') # \x1B[26;1H
    print("[M] Main Menu   [Q] Quit")
    print(">>> ", end='')
MOVE_TO_LOGIN_EMAIL_INPUT = lambda: print("\x1B[3J\x1B[100A\x1B[23B\u2502Email: ", end='') # \x1B[22;8H
MOVE_TO_LOGIN_PASSWORD_INPUT = lambda: print("\x1B[3J\x1B[100A\x1B[24B\u2502Password: ", end='') # \x1B[23;12H






'''
  ____  _____ ____ _____ ___ ___  _   _              ____ _                         
 / ___|| ____/ ___|_   _|_ _/ _ \| \ | |_           / ___| | __ _ ___ ___  ___  ___ 
 \___ \|  _|| |     | |  | | | | |  \| (_)         | |   | |/ _` / __/ __|/ _ \/ __|
  ___) | |__| |___  | |  | | |_| | |\  |_          | |___| | (_| \__ \__ \  __/\__ \\
 |____/|_____\____| |_| |___\___/|_| \_(_)          \____|_|\__,_|___/___/\___||___/
                                                                                    
'''

class UsersTable:
    
    column_index_dict = {
        'user_id':0,
        'first_name':1,
        'last_name':2,
        'phone':3,
        'email':4,
        'password':5,
        'date_created':6,
        'hire_date':7,
        'user_type':8,
        'active':9
    }
    
    def __init__(self, cursor, column):
        self.row_objects_dict = {}
        row_index = self.column_index_dict[column]
        for row in cursor.execute("SELECT * FROM Users"):
                self.row_objects_dict[row[row_index]] = row
        
    def search_rows(self, search_term, search_type='not_exact'):
        new_dict = {}
        dict_to_list = list(self.row_objects_dict)
        if search_type == 'not_exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term in value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
        elif search_type == 'exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term == value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
    
    def return_dict(self):
        return self.row_objects_dict
    



class CompetenciesTable:
    
    column_index_dict = {
        'competency_id':0,
        'name':1,
        'description':2,
        'active':3
    }
    
    def __init__(self, cursor, column):
        self.row_objects_dict = {}
        row_index = self.column_index_dict[column]
        for row in cursor.execute("SELECT * FROM Competencies"):
                self.row_objects_dict[row[row_index]] = row
        
    def search_rows(self, search_term, search_type='not_exact'):
        new_dict = {}
        dict_to_list = list(self.row_objects_dict)
        if search_type == 'not_exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term in value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
        elif search_type == 'exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term == value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
    
    def return_dict(self):
        return self.row_objects_dict



    
class AssessmentsTable:
    
    column_index_dict = {
        'assessment_id':0,
        'competency_id':1,
        'name':2,
        'date_created':3,
        'active':4
    }
    
    def __init__(self, cursor, column):
        self.row_objects_dict = {}
        row_index = self.column_index_dict[column]
        for row in cursor.execute("SELECT * FROM Assessments"):
                self.row_objects_dict[row[row_index]] = row
        
    def search_rows(self, search_term, search_type='not_exact'):
        new_dict = {}
        dict_to_list = list(self.row_objects_dict)
        if search_type == 'not_exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term in value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
        elif search_type == 'exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term == value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
    
    def return_dict(self):
        return self.row_objects_dict
    
    
class AssessmentResultsTable:
    
    column_index_dict = {
        'results_id':0,
        'user_id':1,
        'assessment_id':2,
        'score':3,
        'date_taken':4,
        'manager_id':5,
        'active':6
    }
    
    def __init__(self, cursor, column):
        self.row_objects_dict = {}
        row_index = self.column_index_dict[column]
        for row in cursor.execute("SELECT * FROM Assessment_Results"):
                self.row_objects_dict[row[row_index]] = row
        
    def search_rows(self, search_term, search_type='not_exact'):
        new_dict = {}
        dict_to_list = list(self.row_objects_dict)
        if search_type == 'not_exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term in value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
        elif search_type == 'exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term == value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
    
    def return_dict(self):
        return self.row_objects_dict

            
        
            
        

class CompetencyLevels:
    
    column_index_dict = {
        'results_id':0,
        'user_id':1,
        'ar_assessment_id':2,
        'score':3,
        'date_taken':4,
        'manager':5,
        'ar_active':6,
        'first_name':7,
        'last_name':8,
        'email':9,
        'assessment_id':10,
        'competency_id':11,
        'name':12,
        'date_created':13,
        'active':14,
        'competency_name':15
    }
    
    def __init__(self, cursor, column):
        self.row_objects_dict = {}
        row_index = self.column_index_dict[column]
        for row in cursor.execute("SELECT ar.results_id, ar.user_id, ar.assessment_id as ar_assessment_id, ar.score, ar.date_taken, ar.manager_id, ar.active as ar_active, u.first_name, u.last_name, u.email, a.assessment_id, a.competency_id, a.name as assessment_name, a.date_created, a.active, c.name as competency_name FROM Assessment_Results ar JOIN Users u ON u.user_id = ar.user_id JOIN Assessments a ON a.assessment_id = ar.assessment_id JOIN Competencies c ON c.competency_id = a.competency_id ORDER BY u.user_id, ar.assessment_id;"):
                self.row_objects_dict[row[row_index]] = row
        
    def search_rows(self, search_term, search_type='not_exact'):
        new_dict = {}
        dict_to_list = list(self.row_objects_dict)
        if search_type == 'not_exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term in value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
        elif search_type == 'exact':
            for index, value in enumerate(dict_to_list):
                value = str(value)
                if search_term == value:
                    new_dict[dict_to_list[index]] = self.row_objects_dict[dict_to_list[index]]
            if new_dict == {}:
                return False
            self.row_objects_dict.clear()
            self.row_objects_dict.update(new_dict)
            return self.row_objects_dict
    
    def return_dict(self):
        return self.row_objects_dict











class ManagerEdit:
    def __init__(self, table):
        load_object()
        self.table = table
        if self.table == 'Users':
            pass
        elif self.table == 'Competencies':
            pass
        elif self.table == 'Assessment':
            pass
        elif self.table == 'Assessment_Results':
            pass









'''
  ____  _____ ____ _____ ___ ___  _   _             _____                 _   _                 
 / ___|| ____/ ___|_   _|_ _/ _ \| \ | |_          |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
 \___ \|  _|| |     | |  | | | | |  \| (_)         | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
  ___) | |__| |___  | |  | | |_| | |\  |_          |  _|| |_| | | | | (__| |_| | (_) | | | \__ \\
 |____/|_____\____| |_| |___\___/|_| \_(_)         |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                                                                                                
'''

def print_and_save_display(print_string='', end='\n', list_mode='no'):
    if list_mode == 'yes':
        print(print_string, end)
        original_stdout = sys.stdout
        with open("saved_display.txt", 'at') as file:
            sys.stdout = file
            print(print_string, end)
        sys.stdout = original_stdout
    elif list_mode == 'no':
        CLEAR_DISPLAY()
        print(print_string, end)
        original_stdout = sys.stdout
        with open("saved_display.txt", 'at') as file:
            sys.stdout = file
            print(print_string, end)
        sys.stdout = original_stdout
    
def print_and_save_menu(print_string='', end='\n'):
    CLEAR_MENU()
    print(print_string, end)
    original_stdout = sys.stdout
    with open("saved_menu.txt", 'at') as file:
        sys.stdout = file
        print(print_string, end)
    sys.stdout = original_stdout

# def new_input(input_string):
#     original_stdout = sys.stdout
#     with open("screen_state.txt", 'at') as file:
#         sys.stdout = file
#         print(input_string)
#     sys.stdout = original_stdout
#     user_input = input(input_string)
#     return user_input

def new_input(input_string=''):
    while True:
        MOVE_TO_INPUT()
        user_input = input(input_string)
        if user_input in ["M", "m"]:
            CLEAR_ALL()
            print_and_save_display(ascii_art.app_label())
            manager_program_start()
        else:
        # if parse_new_input(user_input) == "invalid choice":
        #     continue
        # elif parse_new_input(user_input) == "valid choice":
            return user_input

# def parse_new_input(input):
#     valid_letter_options = ["N", "n", "P", "p", "Q", "q", "B", "b", "A", "a", "M", "m", "VA", "Va", "vA", "va", "VC", "Vc", "vC", "vc", "EP", "Ep", "eP", "ep"]
#     input_type = 0 # 0 means input is a number. 1 means input is a letter.
#     try:
#         int(input)
#     except:
#         input_type += 1
#     if input_type == 1:
#         if input not in valid_letter_options:
#             return "invalid choice"
#         else:
#             return "valid choice"
#     else:
#         input = int(input)
#     if input in range(1,9):
#         return "valid choice"
#     else:
#         return "invalid choice"

# def new_getpass(input_string):
#     original_stdout = sys.stdout
#     with open("screen_state.txt", 'at') as file:
#         sys.stdout = file
#         print(input_string)
#     sys.stdout = original_stdout
#     user_input = getpass(input_string)
#     return user_input

def login_email_input():
    MOVE_TO_LOGIN_EMAIL_INPUT()
    user_input = input("")
    return user_input

def login_password_input():
    MOVE_TO_LOGIN_PASSWORD_INPUT()
    print('\u2588')
    print("\x1B[?25l")
    user_input = getpass("")
    return user_input















'''
  _____     _     _        _____                 _   _                   ____  _       _ 
 |_   _|_ _| |__ | | ___  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___  |  _ \| |_ _  / |
   | |/ _` | '_ \| |/ _ \ | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __| | |_) | __(_) | |
   | | (_| | |_) | |  __/ |  _|| |_| | | | | (__| |_| | (_) | | | \__ \ |  __/| |_ _  | |
   |_|\__,_|_.__/|_|\___| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/ |_|    \__(_) |_|
                                                                                         
'''

def compare_rows(obj_1, obj_2):
    listed_row_1 = list(obj_1.values())
    listed_row_2 = list(obj_2.values())
    if listed_row_1 == listed_row_2:
        return True
    else:
        return False
    
    
    
    
def ask_column(obj_dict):
    # row_key = list(obj_dict.keys())
    row_object = pull_object_from_dict(obj_dict)
    print("Choose from the following columns:\n")
    for index, value in enumerate(list(row_object.keys())):
        print(f'[{index + 1}] {value}\n')
    chosen_column = int(input(">>> "))
    chosen_column -= 1
    column_to_update = ''
    for index, value in enumerate(list(row_object.keys())):
        if index == chosen_column:
            column_to_update += value
    return column_to_update




def ask_value(column_name):
    new_value = new_input(f"Enter a new {column_name}: ")
    return new_value




def insert_row(cursor, table_name, insertion_dictionary):
    value_list_from_dict = []
    column_list_from_dict = []
    key_list = list(insertion_dictionary.keys())
    for key in key_list:
        if insertion_dictionary[key] != '':
            value_list_from_dict.append(insertion_dictionary[key])
            column_list_from_dict.append(key)
    question_mark_list = []
    for i in range(len(column_list_from_dict)):
        question_mark_list.append('?')
    question_mark_string = ', '.join(question_mark_list)
    try:
        cursor.execute(f"INSERT into {table_name}({', '.join(column_list_from_dict)}) VALUES({question_mark_string})", value_list_from_dict)
        connection.commit()
    except:
        return False
    return True




def delete_row(cursor, table_name, obj_dict):
    if update_row(cursor, table_name, obj_dict, 'active', '0'):
        return True
    else:
        return False
    
    
    
    
def restore_row(cursor, table_name, obj_dict):
    if update_row(cursor, table_name, obj_dict, 'active', '1'):
        return True
    else:
        return False




def update_row(cursor, table_name, obj_dict, column_to_update, new_value):
    if column_to_update == 'password':
        new_password = new_value
        new_value = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
    row_object = obj_dict
    if type(obj_dict) != sqlite3.Row:
        row_object = pull_object_from_dict(obj_dict)
    columns_list = row_object.keys()
    column_string = ', '.join(columns_list)
    # print(column_string)
    values_list = list(row_object)
    value_to_change = row_object[column_to_update]
    sql_update = f"UPDATE {table_name} SET {column_to_update}=? WHERE {columns_list[0]} = {row_object[0]}"
    # print(sql_update)
    try:
        cursor.execute(sql_update, [new_value])
        connection.commit()
        if column_to_update == 'email' and singletons.CurrentUser.user_type == 'user':
            singletons.CurrentUser.email = new_value
        elif column_to_update == 'password' and singletons.CurrentUser.user_type == 'user':
            singletons.CurrentUser.password = new_password
    except:
        return False
    if column_to_update == 'active' and new_value == '1':
        print(f"Record from the {table_name} Table with a {list(row_object.keys())[0]} of {row_object[0]} was successfully deleted!")
        time.sleep(3)
    elif column_to_update == 'active' and new_value == '0':
        print(f"Record from the {table_name} Table with a {list(row_object.keys())[0]} of {row_object[0]} was successfully restored!")
        time.sleep(3)
    else:
        if singletons.CurrentUser.user_type == 'manager':
            print(f"\nCOLUMN: {column_to_update}, in TABLE: {table_name}, was successfully updated!\n")
        elif singletons.CurrentUser.user_type == 'user':
            print(f"Your {column_to_update} was successfully updated! Changes will reflect on screen momentarily.")
        updated_user = UsersTable(row_factory_cursor, 'user_id')
        try:
            updated_user = updated_user.search_rows(f'{singletons.CurrentUser.user_id}')
        except:
            CLEAR_ALL()
            print("update and load user - problem")
            quit()
        load_user_info(updated_user)
        time.sleep(5)












'''
  _                _                         _   _                    _ 
 | |    ___   __ _(_)_ __     __ _ _ __   __| | | |    ___   __ _  __| |
 | |   / _ \ / _` | | '_ \   / _` | '_ \ / _` | | |   / _ \ / _` |/ _` |
 | |__| (_) | (_| | | | | | | (_| | | | | (_| | | |__| (_) | (_| | (_| |
 |_____\___/ \__, |_|_| |_|  \__,_|_| |_|\__,_| |_____\___/ \__,_|\__,_|
             |___/                                                      
'''

def login_func(row_factory_cursor):
    print_and_save_display(ascii_art.app_label())
    # time.sleep(3)
    users_table_by_email = UsersTable(row_factory_cursor, 'email')
    print_login_menu()
    email_input = login_email_input()
    if email_input.upper() == "Q":
        quit_func()
    password_input = login_password_input()
    if password_input.upper() == "Q":
        quit_func()
    encoded_password_input = password_input.encode()
    user_by_email = users_table_by_email.search_rows(email_input)
    if user_by_email == False:
        return False
    row_object = pull_object_from_dict(user_by_email)
    logged_in_user_id = row_object['user_id']
    singletons.UserLoggedIn.user_id = logged_in_user_id
    singletons.UserLoggedIn.password = password_input
    hashed_password = row_object['password']
    if bcrypt.checkpw(encoded_password_input, hashed_password):
        load_user_info(user_by_email, decrypted_password=password_input)
        return True
    else:
        return False


    
def load_user_info(obj_dictionary=0, decrypted_password=0):
    if obj_dictionary != 0:
        row_object = pull_object_from_dict(obj_dictionary)
        email = row_object['email']
        password = decrypted_password
        if decrypted_password == 0:
            password = singletons.CurrentUser.password
            email = singletons.CurrentUser.email
        singletons.CurrentUser.user_id = str(row_object['user_id'])
        singletons.CurrentUser.first_name = str(row_object['first_name'])
        singletons.CurrentUser.last_name = str(row_object['last_name'])
        singletons.CurrentUser.phone = str(row_object['phone'])
        singletons.CurrentUser.email = email
        singletons.CurrentUser.password = password
        singletons.CurrentUser.date_created = str(row_object['date_created'])
        singletons.CurrentUser.hire_date = str(row_object['hire_date'])
        singletons.CurrentUser.user_type = str(row_object['user_type'])
        singletons.CurrentUser.active = str(row_object['active'])
        singletons.CurrentUser.object = obj_dictionary
        singletons.CurrentObject.object = row_object
    else:
        chosen_id = new_input("Enter a user_id: ")
        selected_users = UsersTable(row_factory_cursor, 'user_id')
        selected_user = selected_users.search_rows(chosen_id, 'exact')
        try:  
            row_keys = list(selected_user.keys())
        except:
            return "user not found"
        row_object = selected_user[row_keys[0]]
        # print(row_object)
        singletons.CurrentUser.user_id = str(row_object['user_id'])
        singletons.CurrentUser.first_name = str(row_object['first_name'])
        singletons.CurrentUser.last_name = str(row_object['last_name'])
        singletons.CurrentUser.phone = str(row_object['phone'])
        singletons.CurrentUser.email = str(row_object['email'])
        singletons.CurrentUser.password = str(row_object['password'])
        singletons.CurrentUser.date_created = str(row_object['date_created'])
        singletons.CurrentUser.hire_date = str(row_object['hire_date'])
        singletons.CurrentUser.user_type = str(row_object['user_type'])
        singletons.CurrentUser.active = str(row_object['active'])
        singletons.CurrentUser.object = row_object
        singletons.CurrentObject.object = row_object
        


def check_user_privileges(do_print='no_print'):
    if do_print == 'print':
        print(singletons.CurrentUser.user_type)
        return singletons.CurrentUser.user_type
    elif do_print == 'no_print':
        return singletons.CurrentUser.user_type












'''
  _____     _     _        _____                 _   _                   ____  _       ____  
 |_   _|_ _| |__ | | ___  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___  |  _ \| |_ _  |___ \ 
   | |/ _` | '_ \| |/ _ \ | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __| | |_) | __(_)   __) |
   | | (_| | |_) | |  __/ |  _|| |_| | | | | (__| |_| | (_) | | | \__ \ |  __/| |_ _   / __/ 
   |_|\__,_|_.__/|_|\___| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/ |_|    \__(_) |_____|
                                                                                                                                                        
'''


def pull_many_objects_from_dict(obj_dictionary):
    row_keys = list(obj_dictionary.keys())
    row_object_list = []
    for row_key in row_keys:
        current_row_object = obj_dictionary[row_key]
        row_object_list.append(current_row_object)
    
    return row_object_list



def pull_object_from_dict(obj_dictionary):
    row_keys = list(obj_dictionary.keys())
    row_object = obj_dictionary[row_keys[0]]
    return row_object




def print_row_objects_to_text_file(obj_dictionary, table_name, page, exclude=None): # Type the column names you want to exclude in closed square brackets, or leave 'exlclude' unchanged if you want all columns printed.
    formatting_dict = {}
    width_values_dict = {}
    included_index_list = []
    objects_list = list(obj_dictionary.values())
    # print_and_save_display(objects_list)
    header_list = list(objects_list[0].keys())
    # print_and_save_display(header_list)
    if exclude != None:
        for index, header in enumerate(header_list):
            if header not in exclude:
                included_index_list.append(index)
    # print_and_save_display(included_index_list)
    for i in range(len(objects_list)):
        object = objects_list[i]
        for j in included_index_list:
            if i == 0:
                formatting_dict[header_list[j]] = []
            formatting_dict[header_list[j]].append(str(object[j]))
    # print_and_save_display(formatting_dict)
    formatting_dict_keys_list = list(formatting_dict.keys())
    # print_and_save_display(formatting_dict_keys_list)
    for key in formatting_dict_keys_list:
        formatting_dict[key].insert(0, key)
    for key in formatting_dict_keys_list:
        values = formatting_dict[key]
        max_length = len(max(values, key=len))
        width_values_dict[key] = max_length
    list_of_header_list_items_after_adding_trailing_spaces = []
    for i in included_index_list:
        current_header_width = width_values_dict[header_list[i]] + 2
        list_of_header_list_items_after_adding_trailing_spaces.append(header_list[i].ljust(current_header_width))
    header_string = ''.join(list_of_header_list_items_after_adding_trailing_spaces)
    # print_and_save_display(header_string)
    dashes_list = []
    for i in range(len(header_string)):
        dashes_list.append('-')
    dashes_string = ''.join(dashes_list)
    
    # Outputs stdout to a text file to save table for pagination.
    original_stdout = sys.stdout
    with open('current_table.txt', 'w') as f:
        sys.stdout = f
        
        print(header_string)
        print(dashes_string)
        for i in range(len(objects_list)):
            loop_number = 0
            for j in included_index_list:
                if (loop_number + 1) == len(included_index_list):
                    print(str(objects_list[i][header_list[j]]).ljust(width_values_dict[header_list[j]] + 2))
                else:
                    print(str(objects_list[i][header_list[j]]).ljust(width_values_dict[header_list[j]] + 2), end='')
                    loop_number += 1
        print(dashes_string)
                    
    sys.stdout = original_stdout
    



def print_stored_table_by_page():
    table_name = singletons.TablePage.table
    page = singletons.TablePage.page
    if table_name == 'none':
        print("no table loaded")
        return
    elif table_name == 'Users':
        print_and_save_display(ascii_art.users_label())
    elif table_name == 'Competencies':
        print_and_save_display(ascii_art.competencies_label())
    elif table_name == 'Assessments':
        print_and_save_display(ascii_art.assessments_label())
    elif table_name == 'Assessment_Results':
        print_and_save_display(ascii_art.assessment_results_label())
    with open(f'current_table.txt') as f:
        lines = f.readlines()
        index_list = []
        for index, line in enumerate(lines):
            index_list.append(index)
            range_start = ((int(page) * 5) - 5) + 2
            range_end = (int(page) * 5) + 2
            if index in range(range_start, range_end) or index in range(2):
                line = line.strip()
                print_and_save_display(line, end='', list_mode='yes')
        for index, line in enumerate(lines):
            if index == max(index_list):
                print_and_save_display(line.strip(), end='', list_mode='yes')
        if max(index_list) % 5 == 0:
            print_and_save_display(f'Page {page} of {(max(index_list) - 3) // 5}     [N] Next  [P] Previous\n', end='', list_mode='yes')
            singletons.TablePage.page_max = (max(index_list) - 3) // 5
        else:
            print_and_save_display(f'Page {page} of {((max(index_list) -3) // 5) + 1}     [N] Next  [P] Previous\n', end='', list_mode='yes')
            singletons.TablePage.page_max = ((max(index_list) -3) // 5) + 1




def change_table_page(change_choice):
    try:
        if change_choice.upper() == 'N':
            singletons.TablePage.page += 1
            if singletons.TablePage.page_max < singletons.TablePage.page:
                singletons.TablePage.page -= 1
        elif change_choice.upper() == 'P':
            singletons.TablePage.page -= 1
            if singletons.TablePage.page < 1:
                singletons.TablePage.page += 1
        elif change_choice not in ['N', 'P']:
            return "redirect to the quit function"
        return "page_number_selected"
    except:
        return "redirect to a menu function"





def print_saved_menu():
    lines_list = []
    get_lines = 0
    line_count = 0
    with open("screen_state.txt") as file:
        lines = file.readlines()
        index_list = []
        for index, line in enumerate(lines):
            index_list.append(index)
            if line.startswith('Choose'):
                get_lines = 1
            if get_lines == 1 and line_count < 8:
                line_count += 1
                line = line.strip()
                lines_list.append(line)
    for i in range(len(lines_list)):
        print_and_save_menu(lines_list[i], end='')
                
                
                
                
                
def clear_screen_saves():
    with open("saved_display.txt", "wt") as file:
        file.write("")
    with open("saved_menu.txt", "wt") as file:
        file.write("")













'''
  __  __ _              _ _                                    _____                     
 |  \/  (_)___  ___ ___| | | __ _ _ __   ___  ___  _   _ ___  |  ___|   _ _ __   ___ ___ 
 | |\/| | / __|/ __/ _ \ | |/ _` | '_ \ / _ \/ _ \| | | / __| | |_ | | | | '_ \ / __/ __|
 | |  | | \__ \ (_|  __/ | | (_| | | | |  __/ (_) | |_| \__ \ |  _|| |_| | | | | (__\__ \\
 |_|  |_|_|___/\___\___|_|_|\__,_|_| |_|\___|\___/ \__,_|___/ |_|   \__,_|_| |_|\___|___/
                                                                                         
'''

def fix_competency_levels_dicts(single_object):
    fixed_object_dict = {
        'results_id':single_object[0],
        'user_id':single_object[1],
        'assessment_id':single_object[2],
        'score':single_object[3],
        'date_taken':single_object[4],
        'manager':single_object[5],
        'active':single_object[6],
        'first_name':single_object[8],
        'last_name':single_object[9],
        'email':single_object[10],
        'competency_id':single_object[12],
        'assessment_name':single_object[13],
        'date_created':single_object[14],
        'competency_name':single_object[16]
    }
    return fixed_object_dict
    







def view_competency_levels():
    fixed_objects_list = []
    final_dict = {}
    assessment_results_by_results_id = CompetencyLevels(row_factory_cursor, 'results_id')
    assessment_results_by_results_id = assessment_results_by_results_id.return_dict()
    objects_list = pull_many_objects_from_dict(assessment_results_by_results_id)
    for object in objects_list:
        if str(object['user_id']) == singletons.CurrentUser.user_id:
            fixed_object = object
            # if fixed_object['user_id'] == singletons.CurrentUser.user_id:
            fixed_objects_list.append(fixed_object)
    for index, value in enumerate(fixed_objects_list):
        final_dict[index] = value
    return final_dict
            
            
            
            
            
    # competency_levels_dict = {}
    # for object in fixed_objects_list:
    #     try:
    #         competency_levels_dict[object['competency_name']] = {}
    #     except:
    #         print("skip")
    # for object in fixed_objects_list:
    #     try:
    #         competency_levels_dict[object['competency_name']][object['assessment_name']] = {}
    #     except:
    #         print("skip")
    # for object in fixed_objects_list:
    #         competency_levels_dict[object['competency_name']][object['assessment_name']][object['results_id']] = [object['score'], object['date_taken']]



def load_object():
    pass
    
    
def user_view_competency_info():
        
    competency_info = view_competency_levels() # users.return_dict()
    
    print_row_objects_to_text_file(competency_info, 'Competencies', 1, ['results_id', 'user_id', 'ar_assessment_id', 'manager_id', 'ar_active', 'first_name', 'last_name', 'email', 'assessment_id', 'competency_id', 'date_created', 'active'])
    print_stored_table_by_page()
        
    
    
    
    
def check_terminal_size():
    columns, lines = shutil.get_terminal_size()
    print(f'Window Height: {lines}')
    print(f'Window Width: {columns}')
    terminal_size_dict = {
        'width':int(columns),
        'height':int(lines)
    }
    if terminal_size_dict['height'] < 35 or terminal_size_dict['width'] < 140:
        print("ERROR: Terminal window must be bigger.\n")
        print("Note: Height (lines) must be at least 50.\n"
              "      Width (columns) must be at least 150.\n")
        print("IMPORTANT: If height says 24 and width says 80 even after making window much bigger,\nbypass the check below.\n")
        bypass = input("[ENTER] Quit to Resize Window\n"
                       "[B] Bypass\n"
                       ">>> ")
        if bypass.upper() == "B":
            main_program()
            quit()
        else:
            quit()
    else:
        return True





def update_in_editor(field, table):
    MOVE_TO_INPUT()
    print('\x1B[1K')
    new_value = input(f"\n<Hit ENTER w/o entry to Abort>\nEnter New {field}: ")
    if new_value == '':
        return "operation aborted"
    # print("\x1B[2A\x1B[K")
    field = field.lower()
    update_row(cursor, table, singletons.CurrentUser.object, field, new_value)













'''
  __  __                    ____       _       _                
 |  \/  | ___ _ __  _   _  |  _ \ _ __(_)_ __ | |_ ___ _ __ ___ 
 | |\/| |/ _ \ '_ \| | | | | |_) | '__| | '_ \| __/ _ \ '__/ __|
 | |  | |  __/ | | | |_| | |  __/| |  | | | | | ||  __/ |  \__ \\
 |_|  |_|\___|_| |_|\__,_| |_|   |_|  |_|_| |_|\__\___|_|  |___/
                                                                
'''

def manager_main_menu_printer():
    print_and_save_menu(f"Choose From The Following:\n"
                            f"{singletons.Box.ul_corner}{singletons.Box.horizontal_pipe * 128}{singletons.Box.ur_corner}\n"
                        f"{singletons.Box.vertical_pipe}[1] View Table               [3] View Reports                    [5] Add Records                     [7] Delete Records  {singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.vertical_pipe}[2] Edit Records             [4] Search Records                  [6] View Assessments by User        [8] Export/Import   {singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.bl_corner}{singletons.Box.horizontal_pipe * 128}{singletons.Box.br_corner}\n"
                        "\n[Q] Quit\n"
                        ">>> ")
    


def manager_table_choice_menu_printer():
    print_and_save_menu(f"Choose a table to load:\n"
                            f"{singletons.Box.ul_corner}{singletons.Box.horizontal_pipe * 68}{singletons.Box.ur_corner}\n"
                        f"{singletons.Box.vertical_pipe}  [1] Users                    [2] Competencies            {singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.vertical_pipe}  [3] Assessments              [4] Assessment Results      {singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.bl_corner}{singletons.Box.horizontal_pipe * 68}{singletons.Box.br_corner}\n"
                        "\n[Q] Quit\n"
                        ">>> ")






    

def user_main_menu_printer():
    print_and_save_menu(f"Choose From The Following:\n"
                            f"{singletons.Box.ul_corner}{singletons.Box.horizontal_pipe * 68}{singletons.Box.ur_corner}\n"
                        f"{singletons.Box.vertical_pipe}  [EP] Edit Profile                   [VA] View Assessment Results  {singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.vertical_pipe}                                                                    {singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.bl_corner}{singletons.Box.horizontal_pipe * 68}{singletons.Box.br_corner}\n"
                        "\n[Q] Quit\n"
                        ">>> ")



def print_login_menu():
    spacing_string_1 = " " * 43
    spacing_string_2 = " " * 40
    print_and_save_menu(f"Please Login:\n"
                            f"{singletons.Box.ul_corner}{singletons.Box.horizontal_pipe * 50}{singletons.Box.ur_corner}\n"
                        f"{singletons.Box.vertical_pipe}Email: {spacing_string_1}{singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.vertical_pipe}Password: {spacing_string_2}{singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.bl_corner}{singletons.Box.horizontal_pipe * 50}{singletons.Box.br_corner}\n"
                        "\n[Q] Quit\n")
    
    
def print_login_succeeded():
    spacing_string_1_1 = " " * 17
    spacing_string_1_2 = " " * 17
    spacing_string_2_1 = " " * 19
    spacing_string_2_2 = " " * 19
    print_and_save_menu("\n"
                            f"{singletons.Box.ul_corner}{singletons.Box.horizontal_pipe * 50}{singletons.Box.ur_corner}\n"
                        f"{singletons.Box.vertical_pipe}{spacing_string_1_1}Login Successful{spacing_string_1_2}{singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.vertical_pipe}{spacing_string_2_1}--Welcome!--{spacing_string_2_2}{singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.bl_corner}{singletons.Box.horizontal_pipe * 50}{singletons.Box.br_corner}\n"
                        "\n[Q] Quit\n")

def print_login_failed():
    spacing_string_1_1 = " " * 19
    spacing_string_1_2 = " " * 19
    spacing_string_2_1 = " " * 13
    spacing_string_2_2 = " " * 13
    print_and_save_menu("\n"
                            f"{singletons.Box.ul_corner}{singletons.Box.horizontal_pipe * 50}{singletons.Box.ur_corner}\n"
                        f"{singletons.Box.vertical_pipe}{spacing_string_1_1}Login Failed{spacing_string_1_2}{singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.vertical_pipe}{spacing_string_2_1}Incorrect Email/Password{spacing_string_2_2}{singletons.Box.vertical_pipe}\n"
                        f"{singletons.Box.bl_corner}{singletons.Box.horizontal_pipe * 50}{singletons.Box.br_corner}\n"
                        "\n[Q] Quit\n")



def user_profile_editor_printer():
    
    f_1 = singletons.CurrentUser.user_id
    f_2 = singletons.CurrentUser.user_type
    f_1_2 = f'  user_id: {f_1}'
    f_2_2 = f' user_type: {f_2}'
    f_1_f_2 = f'{f_1_2.ljust(34)}│{f_2_2}'
    row_1 = f"{f_1_f_2:68}"
    f_3 = singletons.CurrentUser.date_created
    f_4 = singletons.CurrentUser.hire_date
    f_4_2 = f'    hired: {f_4}'
    f_3_2 = f'   created: {f_3}'
    f_3_f_4 = f'{f_4_2.ljust(34)}│{f_3_2}'
    row_2 = f"{f_3_f_4:68}"
    f_5 = singletons.CurrentUser.first_name
    f_6 = singletons.CurrentUser.last_name
    f_5_2 = f'   f_name: {f_5}'
    f_6_2 = f'    l_name: {f_6}'
    f_5_f_6 = f'{f_5_2.ljust(34)}│{f_6_2}'
    row_3 = f"{f_5_f_6:68}"
    f_7 = singletons.CurrentUser.phone
    f_8 = singletons.CurrentUser.active
    f_7_2 = f'    phone: {f_7}'
    f_8_2 = f'    active: {f_8}'
    f_7_f_8 = f'{f_7_2.ljust(34)}│{f_8_2}'
    row_4 = f"{f_7_f_8:68}"
    
    f_9 = f'        email: {singletons.CurrentUser.email:53}'
    f_0 = f'     password: {singletons.CurrentUser.password:53}'
    
    
    print("\x1B[?25h")
    CLEAR_DISPLAY()
    CLEAR_MENU()
    CLEAR_ALL()
    print_and_save_display("      ____             __ _ _        _____    _ _ _               \n"
            "     |  _ \ _ __ ___  / _(_) | ___  | ____|__| (_) |_ ___  _ __ _ \n"
            "     | |_) | '__/ _ \| |_| | |/ _ \ |  _| / _` | | __/ _ \| '__(_)\n"
            "     |  __/| | | (_) |  _| | |  __/ | |__| (_| | | || (_) | |   _ \n"
            "     |_|   |_|  \___/|_| |_|_|\___| |_____\__,_|_|\__\___/|_|  (_)\n"
            "                                                              \n"
            "Cannot Edit:                                                  \n"
            "┌──────────────────────────────────┬──────────────────────────────────┐\n"
            f"│{row_1} │\n"
            f"│{row_2} │\n"
            f"│{row_3} │\n"
            f"│{row_4} │\n"
            "└──────────────────────────────────┴──────────────────────────────────┘\n"
            "Can Edit:                                                      \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            f"│{f_9} │\n"
            "│                                                                     │\n"
            f"│{f_0} │\n"
            "└─────────────────────────────────────────────────────────────────────┘\n")
            
            
            
def user_profile_editor_menu():
    print_and_save_menu("                                                               \n"
            "Choose From The Following Options:                             \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            "│      [A] Edit Email                       [B] Edit Password         │\n"
            "└─────────────────────────────────────────────────────────────────────┘\n"
            "                                                               \n"
            "[M] Main Menu [Q] Quit                                         \n"
            ">>> ")





def manager_user_profile_editor_printer():
    
    f_1 = singletons.CurrentUser.user_id
    f_2 = singletons.CurrentUser.user_type
    f_1_2 = f'  user_id: {f_1}'
    f_2_2 = f' user_type: {f_2}'
    f_1_f_2 = f'{f_1_2.ljust(34)}{f_2_2}'
    row_1 = f"{f_1_f_2:68}"
    f_3 = singletons.CurrentUser.date_created
    f_4 = singletons.CurrentUser.hire_date
    f_4_2 = f'    hired: {f_4}'
    f_3_2 = f'   created: {f_3}'
    f_3_f_4 = f'{f_4_2.ljust(34)}{f_3_2}'
    row_2 = f"{f_3_f_4:68}"
    f_5 = singletons.CurrentUser.first_name
    f_6 = singletons.CurrentUser.last_name
    f_5_2 = f'   f_name: {f_5}'
    f_6_2 = f'    l_name: {f_6}'
    f_5_f_6 = f'{f_5_2.ljust(34)}{f_6_2}'
    row_3 = f"{f_5_f_6:68}"
    f_7 = singletons.CurrentUser.phone
    f_8 = singletons.CurrentUser.password
    f_7_2 = f'    phone: {f_7}'
    f_8_2 = f'  password: < ENCRYPTED >'
    f_7_f_8 = f'{f_7_2.ljust(34)}{f_8_2}'
    row_4 = f"{f_7_f_8:68}"
    f_9 = singletons.CurrentUser.email 
    f_0 = ''
    f_9_2 = f'    email: {f_9}'
    f_0_2 = f'{f_0}'
    f_9_f_0 = f'{f_9_2.ljust(34)}{f_0_2}'
    row_5 = f"{f_9_f_0:68}"
    
    print("\x1B[?25h")
    CLEAR_DISPLAY()
    CLEAR_MENU()
    CLEAR_ALL()
    print_and_save_display("                   _____    _ _ _               \n"
                           "                  | ____|__| (_) |_ ___  _ __ _ \n"
                           "                  |  _| / _` | | __/ _ \| '__(_)\n"
                           "                  | |__| (_| | | || (_) | |   _ \n"
                           "                  |_____\__,_|_|\__\___/|_|  (_)\n"
                           "                                                \n"
            "                                                                       \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            f"│{row_1} │\n"
            "│                                                                     │\n"
            f"│{row_2} │\n"
            "│                                                                     │\n"
            f"│{row_3} │\n"
            "│                                                                     │\n"
            f"│{row_4} │\n"
            "│                                                                     │*\n"
            f"│{row_5} │\n"
            "└─────────────────────────────────────────────────────────────────────┘")
            
            
            
def manager_user_profile_editor_menu():
    print_and_save_menu("                                                               \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            "│ [1] f_name         [2] l_name        [3] phone         [4] email    │\n"
            "│ [5] date_created   [6] hire_date     [7] user_type                  │\n"
            "└─────────────────────────────────────────────────────────────────────┘\n"
            "                                                               \n"
            "[M] Main Menu [Q] Quit                                         \n"
            ">>> ")







def manager_competency_editor_printer():
    
    f_1 = singletons.CurrentCompetency.competency_id
    f_2 = singletons.CurrentCompetency.name
    f_1_2 = f'  competency_id: {f_1}'
    f_2_2 = f' competency_name: {f_2}'
    f_1_f_2 = f'{f_1_2.ljust(34)}{f_2_2}'
    row_1 = f"{f_1_f_2:68}"
    f_4 = singletons.CurrentCompetency.description
    f_4_2 = f'    description: {f_4}'
    f_3_f_4 = f'{f_4_2.ljust(34)}'
    row_2 = f"{f_3_f_4:68}"
    
    
    print("\x1B[?25h")
    CLEAR_DISPLAY()
    CLEAR_MENU()
    CLEAR_ALL()
    print_and_save_display("                   _____    _ _ _               \n"
                           "                  | ____|__| (_) |_ ___  _ __ _ \n"
                           "                  |  _| / _` | | __/ _ \| '__(_)\n"
                           "                  | |__| (_| | | || (_) | |   _ \n"
                           "                  |_____\__,_|_|\__\___/|_|  (_)\n"
                           "                                                \n"
            "                                                                       \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            f"│{row_1} │\n"
            "│                                                                     │\n"
            f"│{row_2} │\n"
            "│                                                                     │\n"
            "│                                                                     │\n"
            "│                                                                     │\n"
            "│                                                                     │\n"
            "│                                                                     │@\n"
            "│                                                                     │\n"
            "└─────────────────────────────────────────────────────────────────────┘")
            
            
            
def manager_competency_editor_menu():
    print_and_save_menu("                                                               \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            "│          [1] competency_name          [2] description               │\n"
            "└─────────────────────────────────────────────────────────────────────┘\n"
            "                                                               \n"
            "[M] Main Menu [Q] Quit                                         \n"
            ">>> ")








def manager_assessment_editor_printer():
    
    f_1 = singletons.CurrentAssessment.assessment_id
    f_2 = singletons.CurrentAssessment.competency_id
    f_1_2 = f'  assessment_id: {f_1}'
    f_2_2 = f' competency_id: {f_2}'
    f_1_f_2 = f'{f_1_2.ljust(34)}{f_2_2}'
    row_1 = f"{f_1_f_2:68}"
    f_3 = singletons.CurrentAssessment.date_created
    f_4 = singletons.CurrentAssessment.name
    f_3_2 = f'    date_created: {f_3}'
    f_4_2 = f'    name: {f_4}'
    f_3_f_4 = f'{f_4_2.ljust(34)}'
    row_2 = f"{f_3_f_4:68}"
    
    
    print("\x1B[?25h")
    CLEAR_DISPLAY()
    CLEAR_MENU()
    CLEAR_ALL()
    print_and_save_display("                   _____    _ _ _               \n"
                           "                  | ____|__| (_) |_ ___  _ __ _ \n"
                           "                  |  _| / _` | | __/ _ \| '__(_)\n"
                           "                  | |__| (_| | | || (_) | |   _ \n"
                           "                  |_____\__,_|_|\__\___/|_|  (_)\n"
                           "                                                \n"
            "                                                                       \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            f"│{row_1} │\n"
            "│                                                                     │\n"
            f"│{row_2} │\n"
            "│                                                                     │\n"
            "│                                                                     │\n"
            "│                                                                     │\n"
            "│                                                                     │\n"
            "│                                                                     │$\n"
            "│                                                                     │\n"
            "└─────────────────────────────────────────────────────────────────────┘")
            
            
            
def anager_assessment_editor_menu():
    print_and_save_menu("                                                               \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            "│  [1] competency_id        [2] date_created          [3] name        │\n"
            "└─────────────────────────────────────────────────────────────────────┘\n"
            "                                                               \n"
            "[M] Main Menu [Q] Quit                                         \n"
            ">>> ")








    
    
def manager_assessment_results_editor_printer():
    
    f_1 = singletons.CurrentResult.results_id
    f_2 = singletons.CurrentResult.user_id
    f_1_2 = f'  results_id: {f_1}'
    f_2_2 = f' user_id: {f_2}'
    f_1_f_2 = f'{f_1_2.ljust(34)}{f_2_2}'
    row_1 = f"{f_1_f_2:68}"
    f_3 = singletons.CurrentResult.assessment_id
    f_4 = singletons.CurrentResult.score
    f_4_2 = f'    assessment_id: {f_4}'
    f_3_2 = f'   score: {f_3}'
    f_3_f_4 = f'{f_4_2.ljust(34)}{f_3_2}'
    row_2 = f"{f_3_f_4:68}"
    f_5 = singletons.CurrentResult.date_taken
    f_6 = singletons.CurrentResult.manager_id
    f_5_2 = f'   date_taken: {f_5}'
    f_6_2 = f'    manager_id: {f_6}'
    f_5_f_6 = f'{f_5_2.ljust(34)}{f_6_2}'
    row_3 = f"{f_5_f_6:68}"
    
    
    print("\x1B[?25h")
    CLEAR_DISPLAY()
    CLEAR_MENU()
    CLEAR_ALL()
    print_and_save_display("                   _____    _ _ _               \n"
                           "                  | ____|__| (_) |_ ___  _ __ _ \n"
                           "                  |  _| / _` | | __/ _ \| '__(_)\n"
                           "                  | |__| (_| | | || (_) | |   _ \n"
                           "                  |_____\__,_|_|\__\___/|_|  (_)\n"
                           "                                                \n"
            "                                                                       \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            f"│{row_1} │\n"
            "│                                                                     │\n"
            f"│{row_2} │\n"
            "│                                                                     │\n"
            f"│{row_3} │\n"
            "│                                                                     │\n"
            "│                                                                     │\n"
            "│                                                                     │&\n"
            "│                                                                     │\n"
            "└─────────────────────────────────────────────────────────────────────┘")
            
            
            
def manager_assessment_results_editor_menu():
    print_and_save_menu("                                                               \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            "│       [1] score          [2] date_taken          [3] manager_id     │\n"
            "└─────────────────────────────────────────────────────────────────────┘\n"
            "                                                               \n"
            "[M] Main Menu [Q] Quit                                         \n"
            ">>> ")
    

    
















    
# def run_funcs_with_input(initial_input, *funcs):
#     func_storage = []
#     for func in funcs:
#         func_storage.append(func)
#     func_storage_tuple = tuple(func_storage)
#     function_result = 0
#     try:
#         for i in range(len(func_storage_tuple)):
#             if i == 0:
#                 function_result = func_storage[i + 1](func_storage[i](initial_input))
#             else:
#                 function_result = func_storage[i + 1](function_result)
#         return function_result
#     except:
#         return function_result















'''
  ____                __  __       _ _   _       _        _____                     
 |  _ \ _   _ _ __   |  \/  |_   _| | |_(_)_ __ | | ___  |  ___|   _ _ __   ___ ___ 
 | |_) | | | | '_ \  | |\/| | | | | | __| | '_ \| |/ _ \ | |_ | | | | '_ \ / __/ __|
 |  _ <| |_| | | | | | |  | | |_| | | |_| | |_) | |  __/ |  _|| |_| | | | | (__\__ \\
 |_| \_\\__,_|_| |_| |_|  |_|\__,_|_|\__|_| .__/|_|\___| |_|   \__,_|_| |_|\___|___/
                                          |_|                                       
'''

def run_funcs_with_input(initial_input, funcs_list):
    loops = 0
    for func in funcs_list:
        loops += 1
        if loops == 1:
            func(initial_input)
        else:
            func()
            
def run_funcs(funcs_list):
    for func in funcs_list:
            func()

def execute_change_page(initial_input):
    run_funcs_with_input(initial_input, [change_table_page, print_stored_table_by_page])
    
    
def user_profile_editor_screen():
    run_funcs([user_profile_editor_printer, user_profile_editor_menu])
    
    
def user_view_competencies():
    run_funcs([set_table_name, user_view_competency_info])







def set_table_name():
    singletons.TablePage.table = 'Assessment_Results'

    
    
'''
  ___                   _     ____  _               _                    _       
 |_ _|_ __  _ __  _   _| |_  |  _ \(_)_ __ ___  ___| |_ ___  _ __    ___| |_ ___ 
  | || '_ \| '_ \| | | | __| | | | | | '__/ _ \/ __| __/ _ \| '__|  / _ \ __/ __|
  | || | | | |_) | |_| | |_  | |_| | | | |  __/ (__| || (_) | |    |  __/ || (__ 
 |___|_| |_| .__/ \__,_|\__| |____/|_|_|  \___|\___|\__\___/|_|     \___|\__\___|
           |_|                                                                   
'''

def input_director(manager_input_mode=0):
    
    
    
    # Handles manager editing screens:
    while True:
        if manager_input_mode == 1:
            if load_user_info() != "user not found":
                manager_user_profile_editor_printer()
                manager_user_profile_editor_menu()
                
                break
            else:
                print("-User Not Found-")
                time.sleep(2)
                continue
        elif manager_input_mode == 2:
            manager_table_choice_menu_printer()
            break
        else:
            break
    
    
    
    
    
    
    user_input = new_input()
    
    
    
    # Verifies whether 'user_input' is valid for the current screen:
    while True:
        if check_current_menu(user_input) == "valid":
            break
        elif check_current_menu(user_input) == "not valid":
            MOVE_TO_INPUT()
            print('\x1B[1K')
            print("\x1B[?25l")
            print("\x1B[A--Invalid Choice--")
            time.sleep(2)
            print("\x1B[?25h")
            user_input = new_input()
            continue
        
        
    
        
        
    manager_main_menu_option_list = []
    for i in range(1,9):
        i = str(i)
        manager_main_menu_option_list.append(i)
        
    
    
      
        
    # Quit program:
    if user_input.upper() == "Q":
        quit_func()
        
    # Back to Main Menu:
    elif user_input.upper() == "M":
        if singletons.CurrentUser.user_type == 'user':
            # print_and_save_display(ascii_art.app_label())
            # user_main_menu_printer()
            singletons.MenuChoices.user_main_menu = 'M'
            return
        elif singletons.CurrentUser.user_type == 'manager':
            # print_and_save_display(ascii_art.app_label())
            # manager_main_menu_printer()
            singletons.MenuChoices.manager_main_menu = 'M'
            return
    
    
    
    
        
        
    # Change displayed table page:
    elif user_input.upper() in ["N", "P"]:
        execute_change_page(user_input.upper())
    
    # Change user profile info:
    elif user_input.upper() in ["A", "B"]:
        if user_input.upper() == "A":
            MOVE_TO_INPUT()
            print('\x1B[1K')
            new_email = input("\n<Hit ENTER w/o entry to Abort>\nEnter New Email: ")
            if new_email == '':
                return
            # print("\x1B[2A\x1B[K")
            update_row(cursor, 'Users', singletons.CurrentUser.object, "email", new_email)
            # print_and_save_display(ascii_art.app_label())
            # user_main_menu_printer()
            return
        elif user_input.upper() == "B":
            MOVE_TO_INPUT()
            print('\x1B[1K')
            new_password = input("\n<Hit ENTER w/o entry to Abort>\nEnter New Password: ")
            if new_password == '':
                return
            # print("\x1B[2A\x1B[K")
            update_row(cursor, 'Users', singletons.CurrentUser.object, "password", new_password)
            print_and_save_display(ascii_art.app_label())
            user_main_menu_printer()
            return
        
    # User main menu directing:
    elif user_input.upper() in ["VA", "EP"]:
        singletons.MenuChoices.user_main_menu = user_input.upper()
        user_main_menu_director()
        
    # Manager main menu directing:
    elif user_input in manager_main_menu_option_list:
        singletons.MenuChoices.manager_main_menu = user_input
        if user_input == '1':
            manager_table_choice_menu_printer()
        manager_main_menu_director()
        



        

def check_current_menu(current_input):
    temp_lines_storage = []
    with open("saved_menu.txt") as f:
        lines = f.readlines()
        index_list = []
        for index, line in enumerate(lines):
            index_list.append(index)
        range_end = max(index_list) + 1
        range_start = range_end - 10
        for index, line in enumerate(lines):
            if index in range(range_start, range_end):
                line = line.strip()
                temp_lines_storage.append(line)
                
    with open("saved_display.txt") as f:
        lines = f.readlines()
        index_list = []
        for index, line in enumerate(lines):
            index_list.append(index)
        range_end = max(index_list) + 1
        range_start = range_end - 5
        for index, line in enumerate(lines):
            if index in range(range_start, range_end):
                line = line.strip()
                temp_lines_storage.append(line)
                
    currently_valid_choices_list = []
    for line in temp_lines_storage:
        for index, letter in enumerate(line):
            temp_string = ''
            if letter == "[":
                if line[index + 1] in ['E', 'V']:
                    temp_string = temp_string + f"{line[index + 1]}{line[index + 2]}"
                    currently_valid_choices_list.append(temp_string)
                else:
                    temp_string = temp_string + f"{line[index + 1]}"
                    currently_valid_choices_list.append(temp_string)
    # print(currently_valid_choices_list)
    try:
        if current_input.upper() in currently_valid_choices_list or current_input.upper() in ["M", "Q"]:
            # print("valid")
            return "valid"
        else:
            # print("not valid")
            return "not valid"
    except:
        return "not valid"
         
    






def check_current_display(string_list):
    range_end_negative_offset = 0
    range_start_negative_offset = 2
    temp_lines_storage = []
    with open("saved_display.txt") as f:
        lines = f.readlines()
        index_list = []
        for index, line in enumerate(lines):
            index_list.append(index)
        range_end = (max(index_list) + 1) - range_end_negative_offset
        pre_range_start = range_end - 10
        range_start = pre_range_start - range_start_negative_offset
        for index, line in enumerate(lines):
            if index in range(range_start, range_end):
                line = line.strip()
                temp_lines_storage.append(line)
    words = 0
    for i in string_list:
        for j in temp_lines_storage:
            if i in j:
                words += 1
                break
    # print(str(words))
    if words < len(string_list):
        # print("False")
        return False
    else:
        # print("True")
        return True




def check_current_menu_image(string_list):
    range_end_negative_offset = 0
    range_start_negative_offset = 2
    temp_lines_storage = []
    with open("saved_menu.txt") as f:
        lines = f.readlines()
        index_list = []
        for index, line in enumerate(lines):
            index_list.append(index)
        range_end = (max(index_list) + 1) - range_end_negative_offset
        pre_range_start = range_end - 10
        range_start = pre_range_start - range_start_negative_offset
        for index, line in enumerate(lines):
            if index in range(range_start, range_end):
                line = line.strip()
                temp_lines_storage.append(line)
    words = 0
    for i in string_list:
        for j in temp_lines_storage:
            if i in j:
                words += 1
                break
    # print(str(words))
    if words < len(string_list):
        # print("False")
        return False
    else:
        # print("True")
        return True








def manager_submenu_input_director():
    # Mode changer for submenus:
    current_mode = 0
    dict_of_lists = {
        'manager_user_editor':["*"],
        'manager_table_chooser':["[1] Users                    [2] Competencies"]
    }
    mode_key_dict = {
        'manager_user_editor':1,
        'manager_table_chooser':2
    }
    dict_of_lists_keys_list = list(dict_of_lists.keys())
    for key in dict_of_lists_keys_list:
        if check_current_display(dict_of_lists[key]):
            current_mode = mode_key_dict[key]
            break
    for key in dict_of_lists_keys_list:
        if check_current_menu_image(dict_of_lists[key]):
            current_mode = mode_key_dict[key]
            break
    # print(f'current_mode {current_mode}')
    
    return current_mode


    
def return_to_main_menu():
    CLEAR_ALL()
    print_and_save_display(ascii_art.app_label())
    manager_program_start()








'''
  __  __                    ____  _               _                 
 |  \/  | ___ _ __  _   _  |  _ \(_)_ __ ___  ___| |_ ___  _ __ ___ 
 | |\/| |/ _ \ '_ \| | | | | | | | | '__/ _ \/ __| __/ _ \| '__/ __|
 | |  | |  __/ | | | |_| | | |_| | | | |  __/ (__| || (_) | |  \__ \\
 |_|  |_|\___|_| |_|\__,_| |____/|_|_|  \___|\___|\__\___/|_|  |___/
                                                                    
'''

def user_main_menu_director():
    funcs_dict = {
    "EP":user_profile_editor_screen,
    "VA":user_view_competencies
}
    while True:
        menu_choice = singletons.MenuChoices.user_main_menu
        if menu_choice == 'M':
            CLEAR_ALL()
            print_and_save_display(ascii_art.app_label())
            user_program_start()
        elif menu_choice != '':
            funcs_dict[menu_choice]()
            input_director()
            continue
        else:
            print('\x1B[?25h')
            print("\nMike says:\n"
                "\tERROR FOUND in function: 'user_main_menu_director'.\n"
                "\tVariable: 'menu_choice' is taken from class: singletons.MenuChoices.user_main_menu.\n"
                "\tHowever, the above class value given to 'menu_choice' is ''.\n")
            print("Initializing Manual Program Termination")
            time.sleep(2)
            print("Program Terminated")
            quit()
        
        
        
        
def manager_table_choice_screen():
    input_director(2)
        
        
def manager_user_profile_editor_screen():
    input_director(1)
    # run_funcs([load_user_info, manager_user_profile_editor_printer, manager_user_profile_editor_menu])

    
def manager_main_menu_director():
    funcs_dict = {}
    current_mode = manager_submenu_input_director()
    if current_mode == 0:
        funcs_dict = {
            '1':manager_table_choice_screen,
            '2':manager_user_profile_editor_screen
        }
    elif current_mode == 1:
        funcs_dict = {
            '1':table_users_f_name_update,
            '2':table_users_l_name_update,
            '3':table_users_phone_update,
            '4':table_users_email_update,
            '5':table_users_date_created_update,
            '6':table_users_hire_date_update,
            '7':table_users_user_type_update,
            'M':return_to_main_menu,
            'm':return_to_main_menu
        }
    elif current_mode == 2:
        funcs_dict = {
            '1':manager_view_table_users,
            '2':manager_view_table_competencies,
            '3':manager_view_table_assessments,
            '4':manager_view_table_assessment_results
        }
    while True:
        menu_choice = singletons.MenuChoices.manager_main_menu
        if menu_choice == 'M':
            CLEAR_ALL()
            print_and_save_display(ascii_art.app_label())
            manager_program_start()
        elif menu_choice != '':
            funcs_dict[menu_choice]()
            input_director()
            continue
        else:
            print('\x1B[?25h')
            print("\nMike says:\n"
                "\tERROR FOUND in function: 'manager_main_menu_director'.\n"
                "\tVariable: 'menu_choice' is taken from class: singletons.MenuChoices.manager_main_menu.\n"
                "\tHowever, the above class value given to 'menu_choice' is ''.\n")
            print("Initializing Manual Program Termination")
            time.sleep(2)
            print("Program Terminated")
            quit()
        
            
            
# Manager Users editing functions:         
            
def table_users_f_name_update():
    update_in_editor('First_Name', 'Users')
    manager_user_profile_editor_printer()
    manager_user_profile_editor_menu()
    
    
def table_users_l_name_update():
    update_in_editor('Last_Name', 'Users')
    manager_user_profile_editor_printer()
    manager_user_profile_editor_menu()
    
def table_users_phone_update():
    update_in_editor('Phone', 'Users')
    manager_user_profile_editor_printer()
    manager_user_profile_editor_menu()

def table_users_email_update():
    update_in_editor('Email', 'Users')
    manager_user_profile_editor_printer()
    manager_user_profile_editor_menu()
    
def table_users_date_created_update():
    update_in_editor('Date_Created', 'Users')
    manager_user_profile_editor_printer()
    manager_user_profile_editor_menu()

def table_users_hire_date_update():
    update_in_editor('Hire_Date', 'Users')
    manager_user_profile_editor_printer()
    manager_user_profile_editor_menu()
    
def table_users_user_type_update():
    if singletons.UserLoggedIn.user_id == singletons.CurrentUser.user_id:
        update_in_editor('User_Type', 'Users')
        manager_user_profile_editor_printer()
        manager_user_profile_editor_menu()
        quit_func()
    else:
        manager_user_profile_editor_printer()
        manager_user_profile_editor_menu()
        update_in_editor('User_Type', 'Users')



# update_row(cursor, 'Users', singletons.CurrentUser.object, "password", new_password)












'''
  __  __                                     __  __                    _____                     
 |  \/  | __ _ _ __   __ _  __ _  ___ _ __  |  \/  | ___ _ __  _   _  |  ___|   _ _ __   ___ ___ 
 | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__| | |\/| |/ _ \ '_ \| | | | | |_ | | | | '_ \ / __/ __|
 | |  | | (_| | | | | (_| | (_| |  __/ |    | |  | |  __/ | | | |_| | |  _|| |_| | | | | (__\__ \\
 |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|    |_|  |_|\___|_| |_|\__,_| |_|   \__,_|_| |_|\___|___/
                           |___/                                                                 
'''




def manager_view_table_users():
    singletons.MenuChoices.manager_main_menu = '1'
    manager_view_table()
    
def manager_view_table_competencies():
    singletons.MenuChoices.manager_main_menu = '2'
    manager_view_table()

def manager_view_table_assessments():
    singletons.MenuChoices.manager_main_menu = '3'
    manager_view_table()

def manager_view_table_assessment_results():
    singletons.MenuChoices.manager_main_menu = '4'
    manager_view_table()

def manager_view_table():
    items = 0
    while True:
        table = singletons.MenuChoices.manager_main_menu
        if table == '1':
            items = UsersTable(row_factory_cursor, 'user_id')
            items = items.return_dict()
            table = 'Users'
        elif table == '2':
            items = CompetenciesTable(row_factory_cursor, 'competency_id')
            items = items.return_dict()
            table = 'Competencies'
        elif table == '3':
            items = AssessmentsTable(row_factory_cursor, 'assessment_id')
            items = items.return_dict()
            table = 'Assessments'
        elif table == '4':
            items = AssessmentResultsTable(row_factory_cursor, 'results_id')
            items = items.return_dict()
            table = 'Assessment_Results'
        if check_current_menu(table):
            break
    singletons.TablePage.table = table
    
    
    print_row_objects_to_text_file(items, singletons.TablePage.table, 1, ['active'])
    print_stored_table_by_page()
    
    
    









'''
  __  __       _         ____                                      
 |  \/  | __ _(_)_ __   |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  
 | |\/| |/ _` | | '_ \  | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \ 
 | |  | | (_| | | | | | |  __/| | | (_) | (_| | | | (_| | | | | | |
 |_|  |_|\__,_|_|_| |_| |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|
                                         |___/                     
'''

def main_program():
    
    
    # Login:
    while True:
        do_login = login_func(row_factory_cursor)
        if do_login == True:
            print_login_succeeded()
            time.sleep(2)
            if singletons.CurrentUser.user_type == 'user':
                user_program_start()
                while True:
                    input_director()
            elif singletons.CurrentUser.user_type == 'manager':
                manager_program_start()
                while True:
                    input_director()
        else:
            print_login_failed()
            time.sleep(5)
            CLEAR_ALL()
            print("\x1B[?25h", end='')
            continue


def manager_program_start():
    # print_and_save_display(ascii_art.app_label())
    manager_main_menu_printer()
    print("\x1B[?25h", end='')
    # input_director()
    director_prime()

def user_program_start():
    # print_and_save_display(ascii_art.app_label())
    user_main_menu_printer()
    print("\x1B[?25h", end='')
    # input_director()
    director_prime()
        

        
        


def quit_func():
    CLEAR_ALL()
    print("\x1B[?25l")
    print(ascii_art.goodbye_label())
    for i in range(5,0,-1):
        print(f"Program Terminating in {i}...")
        time.sleep(0.5)
        print("\x1B[2A\x1B[K")
    CLEAR_ALL()
    print("\x1B[?25h")
    clear_screen_saves()
    quit()














def director_prime():
    check_current_menu([])
    























































# ============================================================

# for i in range(27):
#     print("-" * 130)
CLEAR_ALL()
check_terminal_size()
main_program()
# check_current_menu("A")
# user_view_competency_levels()


