dictionary = {
    "hello": "world",
}
number = 25

try:
    number = number + dictionary["hello"]
    print(number)
except Exception as e:
    print(repr(e))
    print("\nMike says:\n"
              "\tERROR FOUND in function: 'manager_main_menu_director'.\n"
              "\tVariable: 'menu_choice' is taken from class: singletons.MenuChoices.manager_main_menu.\n"
              "\tHowever, the above class value given to 'menu_choice' is ''.\n")