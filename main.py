from prettytable import PrettyTable, from_csv, DOUBLE_BORDER
from administration import AdminCommands, Authenticator
from money_manager import Money
from pathlib import Path
import json, os, time, config
from user_interface import LoadingScreen

# Create menu board
def menu_board():
    menu_table = PrettyTable()
    with open(config.CSV_PATH) as file:
        menu_table = from_csv(file)
    menu_table.align = "l"
    menu_table.set_style(DOUBLE_BORDER)
    return menu_table

# Prompt the user to place their order
# order = input("\nWhat do you want to order?\n")
# order_elements = order.lower().split(" ")
# no_choice = ["i", "don't", "know"]


# if all(word in order_elements for word in no_choice):
#     print("That's okay! I would recommend the medium-sized espresso with extra sugar."
#           " Do you like this recommendation? (yes/no)")

def coffee_shop_mode(self):
    
    pass

def admin_mode():
    access_admin = Authenticator()
    proceed_to_admin = False
    want_to_continue = access_admin.choose_continue()
    
    if want_to_continue and access_admin.auth_choice == "1":
        proceed_to_admin = access_admin.verify_password()
    if want_to_continue and access_admin.auth_choice == "2":
        proceed_to_admin = access_admin.verify_2fa()
    
    if not proceed_to_admin:
        return # This should return the enter admin function
        
    still_admin = True
    while still_admin:
        admin_commands = AdminCommands()
        input_code = admin_commands.command_input()
        # if user choose "0" --> exit Admin Mode
        if input_code == "0":
            config.clear()
            LoadingScreen("Exiting Admin Mode, returning to the Cafe", islong=True)
            still_admin = admin_commands.exit_admin()
            continue
        
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
        

if __name__ == '__main__':
    main()