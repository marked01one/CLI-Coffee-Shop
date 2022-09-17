import json

class Admin:
    def __init__(self):
        pass
    
    def authentication(self):
        pass
    
    def add_flavour(self):
        """Add a new flavour to the menu, along with all its specifications"""
        name = input("A new flavour! What will be its name?\n").lower()
        water = int(input("How much water is needed? (ml)\n"))
        milk = int(input("How much milk is needed? (ml)\n"))
        coffee = int(input("How much coffee is needed? (g)\n"))
        prices = [
            float(price) for price in input("Enter its prices like this: small --> medium --> large, separated by spaces:\n").split(" ")
        ]
        
        new_flavour = {
            name: {             
                "water": int(water),
                "milk": int(milk),
                "coffee": int(coffee),
                "price": [prices[0], prices[1], prices[2]]
            }
        }
        
        with open("inventory.json", "r+") as file:
            inventory_dict = json.load(file)
            inventory_dict["flavours"][name] = new_flavour[name]
            file.seek(0)
            json.dump(inventory_dict, file, indent=4)
        
    
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

