import json, pandas, time, config, os
from user_interface import LoadingScreen
from random import *
from prettytable import PrettyTable
from twilio.rest import Client
from EDIT_ME import *



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
     
    def enter_command(self):
        """Prompt the user to input their admin command"""
        self.command = input("\nWhat would you like to do today? Type the corresponding number:\n")
        while self.command not in config.SUPPORTED_COMMAND_PROMPTS:
            config.clear()
            print("Sorry! That command is invalid!")
            time.sleep(0.5)
            print(self.cmd_table)
            self.command = input("\nPlease enter a valid corresponding command number:\n")
        return self.command

    def print_report(self):
        """Print report of current cafe resources to the command line"""
        water = self.inventory_dict["resources"]["water"]
        milk = self.inventory_dict["resources"]["milk"]
        coffee = self.inventory_dict["resources"]["coffee"]
        money = self.inventory_dict["resources"]["money"]
        print("Amount of of each resources:\n")
        print(f"💦 Water: {water} ml")
        print(f"🥛 Milk: {milk} ml")
        print(f"🌱 Coffee: {coffee} g")
        print(f"💰 Revenue: ${money:.02f}\n")

    def refill_resources(self):
        """Refill cafe resources based on user input"""
        self.print_report()
        self.add_water = input("💦 How much water do you want to add, in ml: ", end="\r")
        self.add_milk = input("🥛 How much water do you want to add, in ml: ", end="\r")
        self.add_coffee = input("🌱 How much water do you want to add, in grams: ", end="\r")
        LoadingScreen("Adding resources", islong=True)
        self.inventory_dict["resources"]["water"] += self.add_water
        self.inventory_dict["resources"]["milk"] += self.add_milk
        self.inventory_dict["resources"]["coffee"] += self.add_coffee
        self.print_report()

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

    def change_password(self):
        """Change the password to access Admin Mode"""
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
        """
        Prompt the user to choose whether to continue into Admin Mode
        
        Returns a boolean value to let the program know whether the user wants to continue or not
        """
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
            self.auth_choice = input("Enter 1 for password, enter 2 for 2FA:\n")
        return True
    
   # * Verify the password inputted by the user
    def verify_password(self, input_pw, correct_pw=ADMIN_PASSWORD):
        """Verify whether the user-inputted password is correct or not
        
        Returns:
            boolean: tells the user whether they are qualified to continue to Admin Mode
        """
        while input_pw != correct_pw:
            print("Sorry! That was not the correct password!")
            self.input_pw = input("Enter the password again, or enter 'exit' if you want to return to the cafe:\n")
            if self.input_pw == "exit":
                LoadingScreen("Returning to the Cafe", islong=False)
                return False
        LoadingScreen("Entering Admin Mode", islong=True)
        return True
    
    def create_otp(self):
        ltr_count = randint(4,7)
        letters = [choice(config.LETTERS) for i in range(ltr_count)]
        numbers = [choice(config.NUMBERS) for i in range(10 - ltr_count)]
        self.char_list = letters + numbers
        shuffle(self.char_list)
        self.one_time_pw = "".join(self.char_list)
        
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
                body=
                f"One Time Password for the Cafe's admin mode. DO NOT SHARE WITH ANYONE.\n\nPassword: {self.one_time_pw}",
                from_=TWILIO_PHONE,
                to=ADMIN_PHONE
            )
        LoadingScreen("Sending Two Factor Authentication Code", islong=True)
        return self.one_time_pw

