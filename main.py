from pickle import MARK
from prettytable import PrettyTable, from_csv, DOUBLE_BORDER
from administration import Admin
from money_manager import Money
from random import *
from config import ADMIN_COMMANDS
import json
import os
import time

clear = lambda: os.system('cls')

clear()
print(
"""Welcome to the Marked's Coffee Shop!
Check out our menu below!\n"""
)

# Create menu board
menu_table = PrettyTable()
with open("menu.csv") as menu_csv:
    menu_table = from_csv(menu_csv)
menu_table.align = "l"
menu_table.set_style(DOUBLE_BORDER)
print(menu_table)

# Prompt the user to place their order
order = input("\nWhat do you want to order?\n")
order_elements = order.lower().split(" ")
no_choice = ["i", "don't", "know"]


if all(word in order_elements for word in no_choice):
    print("That's okay! I would recommend the medium-sized espresso with extra sugar."
          " Do you like this recommendation? (yes/no)")


if order == "mode.admin":
    clear()
    for i in range(randint(3,7)):
        for k in range(randint(2,4)):
            print("Loading Authenticator" + "."*k, end="\r")
            time.sleep(0.25)
        clear()
            
    
    print("Welcome to the Administration Room" + "\n")
    
    cmd_table = PrettyTable()
    cmd_table.field_names = ADMIN_COMMANDS["field_names"]
    cmd_table.add_rows(ADMIN_COMMANDS["commands"])
    cmd_table.align["To Execute This Command..."] = "l"
    cmd_table.align["Please Enter:"] = "r"
    print(cmd_table)
    
    command = input("\nWhat would you like to do today? Type the corresponding number:\n")

