import json, pandas, config
from user_interface import LoadingScreen

class CoffeeMaker:
    def __init__(self, flavour, size) -> None:
        # Extract resource & price data from CSV and JSON files
        with open("inventory.json", "r") as file:
            self.inventory_dict = json.load(file)    
        menu_df = pandas.read_csv(config.CSV_PATH, index_col=False)
        price_tags = menu_df[menu_df["Drinks"] == flavour.title()]
        
        # Retrieve the flavour's resources and price from the aforementioned CSV and JSON files 
        self.flavour = flavour
        self.resources = self.inventory_dict["resources"]
        self.flavour_specs = self.inventory_dict["flavours"][flavour]
        self.flavour_price = price_tags[size].to_list()[0]
        
        print(self.resources)
        print(self.flavour_specs)
        print(self.flavour_price)
        pass
    
    
    def make_drink(self):
        """"Create" a drink by deducting the amount of resources required to 
           create that drink from the available inventory"""
        
        for item in self.resources:
            try:
                resources_enough = self.resources[item] < self.flavour_specs[item]
            except KeyError:
                pass
            if resources_enough and item != 'money':
                LoadingScreen(f"Sorry! We are out of {item}! Returning to main menu", islong=False)
                return
            try:
                self.resources[item] -= self.flavour_specs[item]
            except KeyError:
                pass
        LoadingScreen(f"Making your {self.flavour}", islong=True)
        LoadingScreen("Processing your payment", islong=False)
        self.collect_money()
        print(f"☕ Here's your {self.flavour}! Enjoy your drink!")
        
    
    def collect_money(self):
        """Deduct the amount of money of the given flavour and size"""
        self.inventory_dict["resources"]["money"] += self.flavour_price
        with open("inventory.json", "w") as file:    
            json.dump(self.inventory_dict, file, indent=4)
    
coffee_maker = CoffeeMaker("espresso", "Large")
coffee_maker.make_drink()