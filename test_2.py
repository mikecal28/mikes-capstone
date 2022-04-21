def func_a():
    print("This is awesome!")

func_dict = {
    'this_func':func_a
}

# func_dict['this_func']()

# print(func_dict['this_func'])

# =====================================

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
    if current_input.upper() in currently_valid_choices_list or current_input.upper() in ["M", "Q"]:
        # print("valid")
        return "valid"
    else:
        # print("not valid")
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
    print(str(words))
    if words < len(string_list):
        print("False")
        return False
    else:
        print("True")
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
    print(str(words))
    if words < len(string_list):
        print("False")
        return False
    else:
        print("True")
        return True
    


is_user_profile_editor = ["Can Edit:", "email:", "password:"]
is_manager_view_users_table = ["user_id  first_name  last_name  phone           email                       date_created         hire_date            user_type"]
is_manager_user_editor = ["*"]

check_current_display(my_list)
