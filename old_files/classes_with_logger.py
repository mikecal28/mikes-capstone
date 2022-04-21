class SaveScreen(object):
    def __init__(self, filename="Default.log"):
        self.stdout = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.stdout.write(message)
        self.log.write(message)
        self.log.flush()
    
    def flush(self):
        pass



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
        'user_id':0,
        'assessment_id':1,
        'score':2,
        'date_taken':3,
        'manager_id':4,
        'active':5
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

# Singletons ====================================================================================
    
class TablePage:
    table = 'none'
    page = 1

class ViewTable:
    pass
    
# Functions =====================================================================================

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
    new_value = input(f"Enter a new {column_name}: ")
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
    row_object = pull_object_from_dict(obj_dict)
    columns_list = list(row_object.keys())
    column_string = ', '.join(columns_list)
    print(column_string)
    values_list = list(row_object)
    value_to_change = row_object[column_to_update]
    sql_update = f"UPDATE {table_name} SET {column_to_update}=? WHERE {columns_list[0]} = {row_object[0]}"
    print(sql_update)
    try:
        cursor.execute(sql_update, [new_value])
        connection.commit()
    except:
        return False
    if column_to_update == 'active' and new_value == '1':
        print(f"Record from the {table_name} Table with a {list(row_object.keys())[0]} of {row_object[0]} was successfully deleted!")
    elif column_to_update == 'active' and new_value == '0':
        print(f"Record from the {table_name} Table with a {list(row_object.keys())[0]} of {row_object[0]} was successfully restored!")
    else:
        print(f"\nColumn {column_to_update} in the {table_name} Table was successfully updated!\n")

def login_func(row_factory_cursor):
    users_table_by_email = UsersTable(row_factory_cursor, 'email')
    email_input =  'toni.robertson@example.com' # input("Email: ")
    password_input = 'mustang' # getpass("Password: ")
    encoded_password_input = password_input.encode()
    users_table_by_email = users_table_by_email.search_rows(email_input)
    if users_table_by_email == False:
        return False
    row_object = pull_object_from_dict(users_table_by_email)
    hashed_password = row_object['password']
    if bcrypt.checkpw(encoded_password_input, hashed_password):
        current_user_password_unencrypted.append(password_input)
        set_user_privileges(row_object)
        return True
    else:
        return False
    
def set_user_privileges(row_obj):
    user_privilege.append(row_obj['user_type'])
    
def check_user_privileges(do_print='no_print'):
    if do_print == 'print':
        print(user_privilege[0])
        return user_privilege[0]
    elif do_print == 'no_print':
        return user_privilege[0]
    
def pull_object_from_dict(obj_dictionary):
    row_key = list(obj_dictionary.keys())
    row_object = obj_dictionary[row_key[0]]
    return row_object

def print_row_objects(obj_dictionary, table_name, page, exclude=None): # Type the column names you want to exclude in closed square brackets, or leave 'exlclude' unchanged if you want all columns printed.
    formatting_dict = {}
    width_values_dict = {}
    included_index_list = []
    objects_list = list(obj_dictionary.values())
    header_list = list(objects_list[0].keys())
    if exclude != None:
        for index, header in enumerate(header_list):
            if header not in exclude:
                included_index_list.append(index)
    for i in range(len(objects_list)):
        object = objects_list[i]
        for j in included_index_list:
            if i == 0:
                formatting_dict[header_list[j]] = []
            formatting_dict[header_list[j]].append(str(object[j]))
    formatting_dict_keys_list = list(formatting_dict.keys())
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
    dashes_list = []
    for i in range(len(header_string)):
        dashes_list.append('-')
    dashes_string = ''.join(dashes_list)
    
    # Outputs stdout to a text file to save screen state.
    # with open('current_table.txt', 'w') as f:
    #     sys.stdout = f
        
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
                    
    # sys.stdout = dual_stdout
    # print_stored_table_by_page()
    


def print_stored_table_by_page():
    table_name = TablePage.table
    page = TablePage.page
    if table_name == 'Users':
        ascii_art.users_label()
    elif table_name == 'Competencies':
        ascii_art.competencies_label()
    elif table_name == 'Assessments':
        ascii_art.assessments_label()
    elif table_name == 'Assessment_Results':
        ascii_art.assessment_results_label()
    with open(f'current_table.txt') as f:
        lines = f.readlines()
        index_list = []
        for index, line in enumerate(lines):
            index_list.append(index)
            range_start = ((int(page) * 5) - 5) + 2
            range_end = (int(page) * 5) + 2
            if index in range(range_start, range_end) or index in range(2):
                line = line.strip()
                print(line)
        for index, line in enumerate(lines):
            if index == max(index_list):
                print(line.strip())
        if max(index_list) % 5 == 0:
            print(f'Page {page} of {(max(index_list) - 3) // 5}     [N] Next  [P] Previous\n')
        else:
            print(f'Page {page} of {((max(index_list) -3) // 5) + 1}     [N] Next  [P] Previous\n')
        print()
        main_menu_printer()


# ============MANAGER=FUNCTIONS==========================

def main_menu_printer():
    menu_choice = input("Choose From The Following\n"
                        "[1] View Users                      [3] View Reports                    [5] Add Records                     [7] Delete Records \n"
                        "[2] View Assessments by User        [4] Search Records                  [6] Edit Records                    [8] Export/Import\n"
                        "\n[9] Quit\n"
                        ">>> ")
    try:
        int(menu_choice)
    except:
        print("Invalid Entry: Try Again")
        return True
    if int(menu_choice) in range(1,9):
        return menu_choice
    elif int(menu_choice) == 9:
        return False
    else:
        print("Invalid Entry: Try Again")
        return True


def manager_view_users():
    TablePage.table = 'Users'
    users = UsersTable(row_factory_cursor, 'user_id')
    users = users.return_dict()
    print_row_objects(users, 'Users', 1, ['password', 'active'])
    change_table_page(TablePage.table, TablePage.page)
    
        
def change_table_page(table_name, change_page_input, page=1):
    # change_page = input("Page Navigation\n"
    #                     "---------------\n"
    #                     "[N] Next Page\n"
    #                     "[P] Previous Page\n"
    #                     ">>> ")
    if change_page_input.upper() == 'N':
        page += 1
    elif change_page_input.upper() == 'P':
        page -= 1
    elif change_page_input not in ['N', 'P']:
        return False
    CLEAR_ALL()
    print_stored_table_by_page(table_name, page)

# def input_func():
#     user_input = input("\n>>> ")
#     main_menu_choice_list = []
#     for i in range(1,9):
#         main_menu_choice_list.append(str(i))
#     if user_input in main_menu_choice_list:
#         main_menu_choice.clear()
#         main_menu_choice.append(user_input)
#         return True
#     elif user_input == "9":
#         return False
#     elif user_input in ["N", "P", "n", "p"]:
#         CLEAR_ALL()
#         while True:
#             if user_input.upper() == 'N':
#                 currently_displayed_table_and_page_number[1] += 1
#             elif user_input.upper() == 'P':
#                 currently_displayed_table_and_page_number[1] -= 1
#             print_stored_table_by_page()
#             user_input = input("\n>>> ")
#             if user_input not in ["N", "P", "n", "p"]:
#                 # main_menu_choice.append('1')
#                 main_menu_printer()
#                 return True
#             else:
#                 CLEAR_ALL()
#                 continue
#             # return ['table_page', user_input.upper()]
#     else:
#         if user_input == '':
#             print('\x1B[2A\x1B[4D\x1B[K')
#             return True
#         else:
#             print("Invalid Entry: Try Again")
#             return True
    

# ----------------------------------------------------------

def manager_procedure():
    if main_menu_printer() == '1':
        CLEAR_ALL()
        next_choice = manager_view_users()
    if next_choice == 'N':
        pass
        
        
        
# ============USER=FUNCTIONS==========================
    










# ----------------------------------------------------------

def user_procedure():
    pass









# Program ===============================

import bcrypt
import sys
from getpass import getpass
import sqlite3
import ascii_art
import time

dual_stdout = SaveScreen("log_file.txt")
sys.stdout = dual_stdout

    
connection_for_row_factory = sqlite3.connect("capstone_database.db")
connection_for_row_factory.row_factory = sqlite3.Row
row_factory_cursor = connection_for_row_factory.cursor()
connection = sqlite3.connect("capstone_database.db")
cursor = connection.cursor()
CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")
user_privilege = []
current_user_password_unencrypted = []
main_menu_printer_choices = {
    '1':'something'
}

screen_numeber = 0
screen_numeber_list = []



if login_func(row_factory_cursor):
    print("Login Successful!")
else:
    print("Email or Password Incorrect")
    
    
print(f"\nYou have {check_user_privileges()}-level privileges.\n")
time.sleep(3)
CLEAR_ALL()

if check_user_privileges() == 'manager':
    while True:
        if manager_procedure() == False:
            print("Goodbye")
            break
elif check_user_privileges() == 'user':
    while True:
        if user_procedure() == False:
            print("Goodbye")
            break
        
        
        
users = UsersTable(row_factory_cursor, 'user_id')
users = users.return_dict()
print_row_objects(users, ['password'])


