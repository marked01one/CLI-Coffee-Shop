import json

class Resources:
    def __init__(self) -> None:
        with open("invetory.json", "r") as inventory:
            self.resources = json.load(inventory)    
        print(self.resources)
        pass
    
    
    def make_a_drink(self):
        """"Create" a drink by deducting the amount of resources required to 
           create that drink from the available inventory"""
        
        pass