## MODULES
import utils
import db_access


## SYSTEM LOOP
while True:
    valid_menu_choice = False
    user_menu_choice = None 
    
    # get the user's main menu choice
    while not valid_menu_choice:
        user_menu_choice = utils.main_menu()
        if user_menu_choice != None:
            valid_menu_choice = True

    user_option = utils.pick_option(user_menu_choice)
    if user_option == None: break


