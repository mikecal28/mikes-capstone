import sqlite3
from pprint import pprint
from search_function import search_table


# class User:
    
#     def __init__(self, cursor):
#         self.user_id = cursor.execute("SELECT user_id FROM Users")
    
    


def result_set_print():
    pass


def view_table(cursor, table_name):
    columns_list = [description[0] for description in cursor.description]
    # print(columns_list)
    table_return = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
    return_dict = {'sql_cursor_results':table_return, 'columns_list':columns_list}
    return return_dict


def results_to_dict(results_and_column_names_dict):
    # Syntax for paramaters:
    # Parameter 'results_and_column_names_dict': {'sql_cursor_results':<list_of_tuples>, 'columns_list':<list_of_table_column_names>}
    
    fields = results_and_column_names_dict['columns_list']
    sql_cursor_results_dict = {}
    for i in range(len(results_and_column_names_dict['sql_cursor_results'])):
        result_key = f'result_{i + 1}'
        sql_cursor_results_dict[result_key] = {}
        for j in range(len(fields)):
            row = results_and_column_names_dict['sql_cursor_results'][i]
            sql_cursor_results_dict[result_key][fields[j]] = row[j]
    return sql_cursor_results_dict


def print_dict(results_and_column_names_dict, columns_to_not_print=[]): 
    # Syntax for paramaters: 
    # Parameter 'results_and_column_names_dict': {'sql_cursor_results':<list_of_tuples>, 'columns_list':<list_of_table_column_names>}
    # Parameter 'columns_to_not_print': [<list_indices>]
    
    listed_results_and_column_names_dict = list(results_and_column_names_dict)
    header_list = []
    dict_of_lists = {}
    for results_and_column_names_dict_key in listed_results_and_column_names_dict:
        listed_row_dict = list(results_and_column_names_dict[results_and_column_names_dict_key])
        if header_list == []:
            header_list = listed_row_dict
            for row_dict_key in listed_row_dict:
                dict_of_lists[row_dict_key] = []
        if header_list != []:
            for row_dict_key in listed_row_dict:
                dict_of_lists[row_dict_key].append(results_and_column_names_dict[results_and_column_names_dict_key][row_dict_key])
    header_widths_list = []
    for header in header_list:
        header_widths_list.append(len(header))
    list_of_max_widths_of_column_values = []
    for j in header_list:
        string_list = []
        for value in dict_of_lists[j]:
            string_list.append(str(value))
        list_of_max_widths_of_column_values.append(len(max(string_list, key=len)))
    column_widths_list = []
    for index in range(len(header_widths_list)):
        column_widths_list.append(max([header_widths_list[index], list_of_max_widths_of_column_values[index]]))
        list_of_header_list_items_after_adding_trailing_spaces = []
    for index, header in enumerate(header_list):
        current_header_width = column_widths_list[index] + 2
        list_of_header_list_items_after_adding_trailing_spaces.append(header.ljust(current_header_width))
    header_string = ''.join(list_of_header_list_items_after_adding_trailing_spaces)
    dashes_list = []
    for i in range(len(header_string)):
        dashes_list.append('-')
    dashes_string = ''.join(dashes_list)
    print(header_string)
    print(dashes_string)
    list_for_length_measurement = dict_of_lists[header_list[0]]
    for i in range(len(list_for_length_measurement)):
        for j in range(len(header_list)):
            current_column_value = str(dict_of_lists[header_list[j]][i])
            if j == len(header_list) - 1:
                print(current_column_value.ljust(column_widths_list[j] + 2))
            else:
                print(current_column_value.ljust(column_widths_list[j] + 2), end='')


def table_record_insert():
    pass


def table_record_update(cursor):
        table_reference_dict = {'1':'Users', '2':'Competencies', '3':'Assessments', '4':'Assessment_Results'}
        id_reference_dict = {'Users':'user_id', 'Competencies':'competency_id', 'Assessments':'assessment_id', 'Assessment_Results':'assessment_id'}
        chosen_table = input("\nWhich Table?\n"
                            "----------------------\n"
                            "[1] Users\n"
                            "[2] Competencies\n"
                            "[3] Assessments\n"
                            "[4] Assessment Results\n"
                            ">>> ")
        if chosen_table not in ['1', '2', '3', '4']:
            return "-Error Code: 3-"
        
        quick_search_decision = input(f"Would you like to do a quick search on the {table_reference_dict[chosen_table]} table? (Y/N): ")
        cursor.execute(f"SELECT * FROM {table_reference_dict[chosen_table]}").fetchone()
        fields = [description[0] for description in cursor.description]
        if quick_search_decision.upper() == 'Y':
            print("\nQuick Search: Initiated\n")
            print()
            search_results = search_table(cursor, table_reference_dict[chosen_table], fields)
            # print(search_results)
            dict_results = results_to_dict(search_results)
            # print(dict_results)
            print_dict(dict_results)
        else:
            print("\nQuick Search: Skipped\n")
        chosen_id = input(f'Enter a {id_reference_dict[table_reference_dict[chosen_table]]}: ')
        try:
            chosen_row = cursor.execute(f"SELECT * FROM {table_reference_dict[chosen_table]} WHERE {id_reference_dict[table_reference_dict[chosen_table]]} = {chosen_id}").fetchall()
        except:
            return "\n-Error Code: 4-\n"
        chosen_row_dict = results_to_dict({'sql_cursor_results':chosen_row, 'columns_list':fields})
        print()
        print_dict(chosen_row_dict)
        input_string_list = ["\nSelect a Field\n",
                    "--------------\n"]
        for index, value in enumerate(fields):
            input_string_list.append(f"[{index + 1}] {value}\n")
        input_string = ''.join(input_string_list)
        field_to_update = input(input_string)
        field_to_update = int(field_to_update)
        if field_to_update not in range(1, (len(fields) + 1)):
            return "\n-Error Code: 5-\n"
        else:
            sql_update = f"UPDATE {table_reference_dict[chosen_table]} WHERE ? = ?"
            update_values = (fields[field_to_update - 1], input("Enter a new value: "))
            try:
                cursor.execute(sql_update, update_values)
            except:
                return "\nERROR: Update Aborted\n"





# ================================
connection = sqlite3.connect("capstone_database.db")
cursor = connection.cursor()

# results = search_table(cursor, 'Users', ['user_id', 'first_name', 'last_name', 'phone'], {'single':{'column':'user_id', 'operator':'<', 'value':'7'}})
# pprint(results)

# my_dict = results_to_dict(results)
# print_dict(my_dict)
while True:
    update_result = table_record_update(cursor)
    if update_result not in ["\nERROR: Update Aborted\n", "\n-Error Code: 3-\n", "\n-Error Code: 4-\n", "\n-Error Code: 5-\n"]:
        connection.commit()
        break
    else:
        print(update_result)
        try_again = input("Would you like to Try Again? ")
        if try_again != '':
            continue
        else:
            break
