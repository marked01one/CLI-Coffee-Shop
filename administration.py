import json, os
import os
from xmlrpc.client import Boolean
from config import ADMIN_COMMANDS, ADMIN_PASSWORD
from user_interface import LoadingScreen
from random import *
import pandas
clear = lambda: os.system('cls')


class AdminCommands:    
    # * Add a new flavour to the menu
    def add_flavour(self):
        """Add a new flavour to the menu, along with all its specifications"""
        # Prompt the user to name the flavour and open the inventory JSON file
        self.name = input("A new flavour! What will be its name?\n").lower()
        with open("inventory.json", "r+") as file:
            inventory_dict = json.load(file)
            # The program will continually prompt the user until a unique flavour name is given
            while self.name in inventory_dict["flavours"]:
                print("Sorry! That flavour is already in the menu!")
                self.name = input("Please choose a different flavour name:\n").lower()
            # Prompt user to input the rest of the specifications of the flavour
            self.water = int(input("How much water is needed? (ml)\n"))
            self.milk = int(input("How much milk is needed? (ml)\n"))
            self.coffee = int(input("How much coffee is needed? (g)\n"))
            self.prices = [f"{float(price):.02f}" for price in input("Enter its prices like this: small --> medium --> large, separated by spaces:\n").split(" ")]
            # Formatting the specifications into a dictionary which can be added to a JSON file
            new_flavour = {
                self.name: {             
                    "water": int(self.water),
                    "milk": int(self.milk),
                    "coffee": int(self.coffee),
                }
            }
            inventory_dict["flavours"][self.name] = new_flavour[self.name]
            file.seek(0)
            json.dump(inventory_dict, file, indent=4)
        # Format the prices into a CSV friendly format and add the new flavour to the menu.csv file
        new_menu_item = {
            "Drinks":  self.name.title(),
            "Small": [self.prices[0]],
            "Medium": [self.prices[1]],
            "Large": [self.prices[2]],
        }
        menu_df = pandas.DataFrame(new_menu_item)
        menu_df.to_csv("menu.csv", mode='a', index=False, header=False)


    # * Remove a flavour from the menu
    def remove_flavour(self):
        """Remove a specific flavour from the menu, if it exists"""
        with open("inventory.json", "r") as file:
            inventory_dict = json.load(file)
        flavour = input("What flavour do you want to remove?\n").lower()
        # Check whether or not the inputted flavour actually exists
        while flavour not in inventory_dict["flavours"]:
            print("Sorry! It seems that the flavour you're looking for doesn't exist")
            flavour = input("Please choose a different flavour to remove:\n").lower()
        # Delete the flavour from inventory
        del inventory_dict["flavours"][flavour]
        with open("inventory.json", "w") as file:
            json.dump(inventory_dict, file, indent=4)
        # Delete
        menu_df = pandas.read_csv("menu.csv", index_col=False)
        menu_df = menu_df[menu_df.Drinks != flavour.title()]
        menu_df.to_csv("menu.csv", index=False)


    # * Change the password to access Admin Mode
    def change_password(self):
        clarify_old = input("Enter your old password:\n")
        if clarify_old != ADMIN_PASSWORD:
            clear()
            clarify_old = input("That was incorrect! Please enter your old password:\n")
        new_password = input("That was correct! Now enter your new password:\n")
        ADMIN_PASSWORD = new_password


class Authenticator:
    def __init__(self):
        # Load the Admin Mode yes/no choice
        LoadingScreen("Loading Authenticator", islong=False)
        print("You are about to access admin mode.")
    
    def choose_continue(self) -> Boolean:
        continue_to_admin = input("Do you wish to continue? (yes/no)\n").lower()
        # Return the user to the main screen if input is invalid or user choose to return
        if continue_to_admin not in ["yes", "no"]:
            LoadingScreen("Invalid response. Returning to the Cafe", islong=False)
            return False
        if continue_to_admin == "no":
            LoadingScreen("Returning to the Cafe", islong=False)
            return False
        # Prompt the user to choose either enter admin mode w/ password or two factor authentication
        print("Do you want to input the password directly or use two factor authentication?")
        self.auth_choice = input("Enter 1 for password, enter 2 for 2FA:\n")
        while self.auth_choice not in ["1", "2"]:
            clear()
            print("Sorry! Your input was invalid.")
        return True
    
   # * Verify the password inputted by the user
    def verify_password(self) -> Boolean:
        input_password = input("Enter the admin password:\n")
        while input_password != ADMIN_PASSWORD:
            print("Sorry! That was not the correct password!")
            input_password = input("Enter the password again, or enter 'exit' if you want to return to the cafe:\n")
            if input_password == "exit":
                LoadingScreen("Returning to the Cafe", islong=False)
                return False
        LoadingScreen("Entering Admin Mode", islong=True)
        return True
    
    def verify_2fa(self) -> Boolean:
        pass
            
admin = AdminCommands()
admin.add_flavour()
