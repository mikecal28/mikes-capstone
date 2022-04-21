import singletons

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
    f_8 = singletons.CurrentUser.active
    f_7_2 = f'    phone: {f_7}'
    f_8_2 = f'    active: {f_8}'
    f_7_f_8 = f'{f_7_2.ljust(34)}{f_8_2}'
    row_4 = f"{f_7_f_8:68}"
    f_9 = singletons.CurrentUser.email
    f_0 = singletons.CurrentUser.password
    f_9_2 = f'    email: {f_9}'
    f_0_2 = f'  password: {f_0}'
    f_9_f_0 = f'{f_9_2.ljust(34)}{f_0_2}'
    row_5 = f"{f_9_f_0:68}"
    
    print("\x1B[?25h")
    CLEAR_DISPLAY()
    CLEAR_MENU()
    CLEAR_ALL()
    print_and_save_display("                  _____    _ _ _               \n"
                           "                 | ____|__| (_) |_ ___  _ __ _ \n"
                           "                 |  _| / _` | | __/ _ \| '__(_)\n"
                           "                 | |__| (_| | | || (_) | |   _ \n"
                           "                 |_____\__,_|_|\__\___/|_|  (_)\n"
                           "                                               \n"
            "To Choose a Field, Please type it's full field-name:                   \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            f"│{row_1}│\n"
            "│                                                                     │\n"
            f"│{row_2}│\n"
            "│                                                                     │\n"
            f"│{row_3}│\n"
            "│                                                                     │\n"
            f"│{row_4}│\n"
            "│                                                                     │\n"
            f"│{row_5}│\n"
            "└─────────────────────────────────────────────────────────────────────┘\n")
            
            
            
def user_profile_editor_menu():
    print_and_save_menu("                                                               \n"
            "Choose From The Following Options:                             \n"
            "┌─────────────────────────────────────────────────────────────────────┐\n"
            "│      [UA] Edit user_id                    [UB] Edit f_name          │\n"
            "│      [UC] Edit l_name                     [UD] Edit phone           │\n"
            "│      [UE] Edit email                      [UF] Edit password        │\n"
            "│      [UG] Edit date_created               [UH] Edit hire_date       │\n"
            "│      [UI] Edit user_type                  [UJ] Delete User          │\n"
            "└─────────────────────────────────────────────────────────────────────┘\n"
            "                                                               \n"
            "[M] Main Menu [Q] Quit                                         \n"
            ">>> ")
