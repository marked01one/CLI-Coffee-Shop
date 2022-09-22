import json, pandas, time, config
from user_interface import LoadingScreen
from random import *
from prettytable import PrettyTable



class AdminCommands:
    def __init__(self):
        # Welcome sentence
        print("Welcome to the Administration Room" + "\n")

        # Formulate table of commands
        self.cmd_table = PrettyTable()
        self.cmd_table.field_names = config.ADMIN_TABLE["field_names"]
        self.cmd_table.add_rows(config.ADMIN_TABLE["commands"])
        self.cmd_table.align["To Execute This Command..."] = "l"
        self.cmd_table.align["Please Enter:"] = "r"
        print(self.cmd_table)
        
        # Open inventory JSON file
        with open("inventory.json", "r+") as file:
            self.inventory_dict = json.load(file)
     
     # * Prompt the user to input their admin command   
    def command_input(self):
        self.command = input("\nWhat would you like to do today? Type the corresponding number:\n")
        while self.command not in config.SUPPORTED_COMMAND_PROMPTS:
            config.clear()
            print("Sorry! That command is invalid!")
            time.sleep(0.5)
            print(self.cmd_table)
            self.command = input("\nPlease enter a valid corresponding command number:\n")
        return self.command


    # * Print report of current cafe resources
    def print_report(self):
        water = self.inventory_dict["resources"]["water"]
        milk = self.inventory_dict["resources"]["milk"]
        coffee = self.inventory_dict["resources"]["coffee"]
        money = self.inventory_dict["resources"]["money"]
        
        print("Amount of of each resources:\n")
        print(f"💦 Water: {water} ml")
        print(f"🥛 Milk: {milk} ml")
        print(f"🌱 Coffee: {coffee} g")
        print(f"💰 Revenue: ${money:.02f}\n")

  
    # * Refill cafe resources based on user input
    def refill_resources(self):
        self.print_report()
        self.add_water = input("💦 How much water do you want to add, in ml: ", end="\r")
        self.add_milk = input("🥛 How much water do you want to add, in ml: ", end="\r")
        self.add_coffee = input("🌱 How much water do you want to add, in grams: ", end="\r")
        LoadingScreen("Adding resources", islong=True)
        
        self.inventory_dict["resources"]["water"] += self.add_water
        self.inventory_dict["resources"]["milk"] += self.add_milk
        self.inventory_dict["resources"]["coffee"] += self.add_coffee
        
        self.print_report()


    # * Add a new flavour to the menu
    def add_flavour(self):
        """Add a new flavour to the menu, along with all its specifications"""
        # Prompt the user to name the flavour and open the inventory JSON file
        # The program will continually prompt the user until a unique flavour name is given
        self.name = input("A new flavour! What will be its name?\n").lower()
        while self.name in self.inventory_dict["flavours"]:
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
        self.inventory_dict["flavours"][self.name] = new_flavour[self.name]
        with open("inventory.json", "w") as file:
            json.dump(self.inventory_dict, file, indent=4)
        
        # Format the prices into a CSV friendly format and add the new flavour to the menu.csv file
        new_menu_item = {
            "Drinks":  self.name.title(),
            "Small": [self.prices[0]],
            "Medium": [self.prices[1]],
            "Large": [self.prices[2]],
        }
        menu_df = pandas.DataFrame(new_menu_item)
        menu_df.to_csv(config.CSV_PATH, mode='a', index=False, header=False)


    # * Remove a flavour from the menu
    def remove_flavour(self):
        """Remove a specific flavour from the menu, if it exists"""
        # Check whether or not the inputted flavour actually exists
        flavour = input("What flavour do you want to remove?\n").lower()
        while flavour not in self.inventory_dict["flavours"]:
            print("Sorry! It seems that the flavour you're looking for doesn't exist")
            flavour = input("Please choose a different flavour to remove:\n").lower()
        
        # Delete the flavour from inventory
        del self.inventory_dict["flavours"][flavour]
        with open("inventory.json", "w") as file:
            json.dump(self.inventory_dict, file, indent=4)
        
        # Delete flavour from menu board
        menu_df = pandas.read_csv(config.CSV_PATH, index_col=False)
        menu_df = menu_df[menu_df.Drinks != flavour.title()]
        menu_df.to_csv(config.CSV_PATH, index=False)

    # * Change the password to access Admin Mode
    def change_password(self):
        clarify_old = input("Enter your old password:\n")
        if clarify_old != config.ADMIN_PASSWORD:
            config.clear()
            clarify_old = input("That was incorrect! Please enter your old password:\n")
        new_password = input("That was correct! Now enter your new password:\n")
        config.ADMIN_PASSWORD = new_password


    # * Exit Admin Mode:
    def exit_admin(self):
        return False

class Authenticator:
    def __init__(self):
        # Load the Admin Mode yes/no choice
        LoadingScreen("Loading Authenticator", islong=False)
        print("You are about to access admin mode.")
    
    def choose_continue(self):
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
            config.clear()
            print("Sorry! Your input was invalid.")
        return True
    
   # * Verify the password inputted by the user
    def verify_password(self):
        input_password = input("Enter the admin password:\n")
        while input_password != config.ADMIN_PASSWORD:
            print("Sorry! That was not the correct password!")
            input_password = input("Enter the password again, or enter 'exit' if you want to return to the cafe:\n")
            if input_password == "exit":
                LoadingScreen("Returning to the Cafe", islong=False)
                return False
        LoadingScreen("Entering Admin Mode", islong=True)
        return True
    
    def verify_2fa(self):
        pass

