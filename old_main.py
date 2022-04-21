import classes
import app_functions
from app_functions import new_print
from app_functions import new_input
from app_functions import new_getpass
import sqlite3
import time
connection_for_row_factory = sqlite3.connect("capstone_database.db")
connection_for_row_factory.row_factory = sqlite3.Row
row_factory_cursor = connection_for_row_factory.cursor()
connection = sqlite3.connect("capstone_database.db")
cursor = connection.cursor()

CLEAR_ALL = lambda: print("\x1B[3J\x1B[H\x1B[2J")
CLEAR_MENU = lambda: print("\x1B[3J\x1B[20;1H\x1B[J")
# change_display_page = app_functions.run_funcs


if app_functions.login_func(row_factory_cursor):
    new_print("Login Successful!")
else:
    new_print("Email or Password Incorrect")
    
    
new_print(f"\nYou have {app_functions.check_user_privileges()}-level privileges.\n")
time.sleep(3)
CLEAR_ALL()

if app_functions.check_user_privileges() == 'manager':
    while True:
        if app_functions.manager_procedure() == False:
            new_print("Goodbye")
            break
elif app_functions.check_user_privileges() == 'user':
    while True:
        if app_functions.user_procedure() == False:
            new_print("Goodbye")
            break



