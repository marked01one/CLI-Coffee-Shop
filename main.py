from pickle import MARK
from prettytable import PrettyTable, from_csv, DOUBLE_BORDER
from administration import AdminCommands, Authenticator
from money_manager import Money
from config import ADMIN_COMMANDS
import json, os, time

clear = lambda: os.system('cls')
# Create menu board
def create_menu():
    menu_table = PrettyTable()
    with open("menu.csv") as file:
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


def admin_mode():
    access_admin = Authenticator()
    proceed_to_admin = False
    if access_admin.choose_continue() and access_admin.auth_choice == "1":
        proceed_to_admin = access_admin.verify_password()
    if access_admin.choose_continue() and access_admin.auth_choice == "2":
        proceed_to_admin = access_admin.verify_2fa()
    
    if proceed_to_admin == False:
        pass # This should return the enter admin function
        
    
    
    print("Welcome to the Administration Room" + "\n")
    
    cmd_table = PrettyTable()
    cmd_table.field_names = ADMIN_COMMANDS["field_names"]
    cmd_table.add_rows(ADMIN_COMMANDS["commands"])
    cmd_table.align["To Execute This Command..."] = "l"
    cmd_table.align["Please Enter:"] = "r"
    print(cmd_table)
    
    command = input("\nWhat would you like to do today? Type the corresponding number:\n")
    return
    
def main():
    clear()
    print("Welcome to the Marked's Coffee Shop!\nCheck out our menu below!\n")
    print(create_menu())
    order = input("\nWhat do you want to order?\n")
    if order == "mode.admin":
        admin_mode()
        

if __name__ == '__main__':
    main()