import sqlite3
from pprint import pprint



def search_table(cursor, table_name, columns_list, where_condition_dict={}):
    # The 'where_condition_dict' formats are explained on next lines (it supports up to two SQL 'WHERE' conditions):
    # If doing an 'or' clause, format will be: {'or':{'1':{'column':'', 'operator':'', 'value':''}, '2':{'column':'', 'operator':'', 'value':''}}}
    # If doing an 'and' clause, format will be: {'and':{'1':{'column':'', 'operator':'', 'value':''}, '2':{'column':'', 'operator':'', 'value':''}}}
    # If not doing either an 'and' or an 'or' clause, format will be: {'single':{'column':'', 'operator':'', 'value':''}}
    
    if where_condition_dict == {}:
        where_condition_dict = {'single':{}}
        where_condition_dict['single'].update(build_where_condition_dict(columns_list))
        
        print(where_condition_dict)
    
    # try:
    columns = ', '.join(columns_list)
    where_condition_list = list(where_condition_dict)
    # print(f'where_condition_list: {where_condition_list}')
    
    if where_condition_list[0] == 'or':
        search_string = f"SELECT {', '.join(columns_list)} FROM {table_name} WHERE {where_condition_dict['or']['1']['column']} {where_condition_dict['or']['1']['operator']} ? OR {where_condition_dict['or']['2']['column']} {where_condition_dict['or']['2']['operator']} ?"
        # print(search_string)
        
        if where_condition_dict['or']['1']['operator'] == 'LIKE' and where_condition_dict['or']['2']['operator'] == 'LIKE':
            search_return = cursor.execute(search_string, ['%'+where_condition_dict['or']['1']['value']+'%', '%'+where_condition_dict['or']['2']['value']+'%']).fetchall()
        elif where_condition_dict['or']['1']['operator'] == 'LIKE' and where_condition_dict['or']['2']['operator'] != 'LIKE':
            search_return = cursor.execute(search_string, ['%'+where_condition_dict['or']['1']['value']+'%', where_condition_dict['or']['2']['value']]).fetchall()
        elif where_condition_dict['or']['1']['operator'] != 'LIKE' and where_condition_dict['or']['2']['operator'] == 'LIKE':
            search_return = cursor.execute(search_string, [where_condition_dict['or']['1']['value'], '%'+where_condition_dict['or']['2']['value']+'%']).fetchall()
        else:
            search_return = cursor.execute(search_string, [where_condition_dict['or']['1']['value'], where_condition_dict['or']['2']['value']]).fetchall()
        
        
    elif where_condition_list[0] == 'and':
        search_string = f"SELECT {', '.join(columns_list)} FROM {table_name} WHERE {where_condition_dict['and']['1']['column']} {where_condition_dict['and']['1']['operator']} ? AND {where_condition_dict['and']['2']['column']} {where_condition_dict['and']['2']['operator']} ?"
        # print(search_string)
        
        if where_condition_dict['and']['1']['operator'] == 'LIKE' and where_condition_dict['and']['2']['operator'] == 'LIKE':
            search_return = cursor.execute(search_string, ['%'+where_condition_dict['and']['1']['value']+'%', '%'+where_condition_dict['and']['2']['value']+'%']).fetchall()
        elif where_condition_dict['and']['1']['operator'] == 'LIKE' and where_condition_dict['and']['2']['operator'] != 'LIKE':
            search_return = cursor.execute(search_string, ['%'+where_condition_dict['and']['1']['value']+'%', where_condition_dict['and']['2']['value']]).fetchall()
        elif where_condition_dict['and']['1']['operator'] != 'LIKE' and where_condition_dict['and']['2']['operator'] == 'LIKE':
            search_return = cursor.execute(search_string, [where_condition_dict['and']['1']['value'], '%'+where_condition_dict['and']['2']['value']+'%']).fetchall()
        else:
            search_return = cursor.execute(search_string, [where_condition_dict['and']['1']['value'], where_condition_dict['and']['2']['value']]).fetchall()
            
        
    elif where_condition_list[0] == 'single':
        search_string = f"SELECT {', '.join(columns_list)} FROM {table_name} WHERE {where_condition_dict['single']['column']} {where_condition_dict['single']['operator']} ?"
        
        if where_condition_dict['single']['operator'] == 'LIKE':
            search_return = cursor.execute(search_string, ['%'+where_condition_dict['single']['value']+'%']).fetchall()
        else:
            search_return = cursor.execute(search_string, where_condition_dict['single']['value']).fetchall()
    
    return_dict = {'sql_cursor_results':search_return, 'columns_list':columns_list}
    return return_dict
    # except:
        # return "Error Code: Search Function"



def build_where_condition_dict(fields):
    operator_reference_dict = {'1':'<', '2':'>', '3':'=', '4':'LIKE'}
    input_string_list = ["\nSelect a Field\n",
                         "--------------\n"]
    for index, value in enumerate(fields):
        input_string_list.append(f"[{index + 1}] {value}\n")
    input_string = ''.join(input_string_list)
    chosen_field = input(input_string)
    # numbers_list = list(range(1, (len(fields) + 1)))
    # print(numbers_list)
    if int(chosen_field) not in range(1, (len(fields) + 1)):
        # print(list(range(1, (len(fields) + 1))))
        return "\n-Error Code: 1-\n"
    else:
        chosen_operator = input("\nChoose an Operator:\n"
                                "-------------------\n"
                                "[1] 'less than'\n"
                                "[2] 'greater than'\n"
                                "[3] 'equal to'\n"
                                "[4] 'is like'\n")
        if chosen_operator not in ['1', '2', '3', '4']:
            return "\n-Error Code: 2-\n"
        else:
            entered_value = input("Enter a Value: ")
    column = fields[int(chosen_field) - 1]
    operator = operator_reference_dict[chosen_operator]
    return_dict = {'column':column, 'operator':operator, 'value':entered_value}
    return return_dict
