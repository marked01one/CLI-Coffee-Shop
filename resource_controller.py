import json

class CoffeeMaker:
    def __init__(self, flavour, size) -> None:
        with open("inventory.json", "r") as file:
            self.inventory_dict = json.load(file)    
        self.resources = self.inventory_dict["resources"]
        self.flavour_specs = self.inventory_dict["flavours"][flavour]
        pass
    
    
    def make_drink(self):
        """"Create" a drink by deducting the amount of resources required to 
           create that drink from the available inventory"""
        
        pass
    
    def deduct_money(self, flavour, size):
        """Deduct the amount of money of the given flavour and size"""
        pass
    
coffeemaker = CoffeeMaker("espresso")