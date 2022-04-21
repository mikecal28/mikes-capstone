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