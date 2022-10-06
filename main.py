from prettytable import PrettyTable, from_csv, DOUBLE_BORDER
from administration import AdminCommands, Authenticator
from user_interface import LoadingScreen
from coffee_maker import CoffeeMaker
import json, os, time, config


# Create menu board
def menu_board():
    menu_table = PrettyTable()
    with open(config.CSV_PATH) as file:
        menu_table = from_csv(file)
    menu_table.align = "l"
    menu_table.set_style(DOUBLE_BORDER)
    return menu_table

def admin_mode():
    auth = Authenticator()
    proceed_to_admin = False
    want_to_continue = auth.choose_continue()
    
    if want_to_continue and auth.auth_choice == "1":
        pw_input = input("Enter the password:\n")
        proceed_to_admin = auth.verify_password(pw_input)
        
    if want_to_continue and auth.auth_choice == "2":
        correct_pw = auth.create_otp()
        print("A one-time password has been sent to the admin's phone")
        pw_input = input("Enter the one-time password:\n")
        proceed_to_admin = auth.verify_password(pw_input, correct_pw)
    
    if not proceed_to_admin:
        return # This should send the user back to the main menu
        
    still_admin = True
    while still_admin:
        admin_commands = AdminCommands()
        input_code = admin_commands.enter_command()
        # if user choose "0" --> exit Admin Mode
        if input_code == "0":
            config.clear()
            LoadingScreen("Exiting Admin Mode, returning to the Cafe", islong=True)
            still_admin = admin_commands.exit_admin()
            continue
        # If user choose "2" --> print resource report
        if input_code == "1":
            config.clear()
            LoadingScreen("Printing Resources Report", islong=True)
            admin_commands.print_report()
            input("\nEnter anything to return to Admin Room\n")
            continue
        # If user choose "3" --> add a flavour
        if input_code == "3":
            config.clear()
            admin_commands.add_flavour()
            input("\nEnter anything to return to Admin Room\n")
            continue
        # If user choose "4" --> remove a flavour
        if input_code == "4":
            admin_commands.remove_flavour()
            continue  
    return
    
def main():
    close_shop = False
    while not close_shop:
        config.clear()
        print("Welcome to the Marked's Coffee Shop!\nCheck out our menu below!\n")
        print(menu_board())
        order = input("\nWhat do you want to order?\n")
        if order == "mode.admin":
            admin_mode()
            continue
        

if __name__ == '__main__':
    main()