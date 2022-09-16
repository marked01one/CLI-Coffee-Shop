from prettytable import PrettyTable
from administration import Admin
from money_manager import Money
from random import *
import json
import os
import time

clear = lambda: os.system('cls')

clear()
print("""Welcome to the Marked's Coffee Shop!
      Here's our menu!
         """)
order = input("What do you want to order? ").split(" ")



if order[0] == "mode.admin":
    clear()
    for i in range(randint(1,10)):
        for k in range(0,4):
            print("Loading Admin" + "."*k, end="\r")
            time.sleep(0.25)
        clear()
            
    
    admin_commands = input("Welcome to the Administration Room" + "\n"
                           "What would you like to do today?")


