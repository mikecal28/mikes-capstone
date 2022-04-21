def new_print(print_string):
    print(print_string)
    original_stdout = sys.stdout
    with open("screen_state.txt", 'wt') as file:
        sys.stdout = file
        print(print_string)
    sys.stdout = original_stdout
