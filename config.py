from pathlib import Path
import os

# ! DO NOT CHANGE THE OPTIONS BELOW, YOUR INSTANCE WILL BREAK ! #
ADMIN_TABLE = {
    "field_names": ["To Execute This Command...", "Please Enter:"],
    "commands": [
        ["Exit Admin Mode", "0"],
        ["Print resources report", "1"],
        ["Refill resources", "2"],
        ["Add a new flavour", "3"],
        ["Remove a flavour", "4"],   
    ]
}
FLAVOUR_CHECK = {
    "flavour_choice": {
        "flavour": ["espresso", "cappuccino", "latte"],
        "size": ["small", "medium", "large"],
        "sugar": {
            "None": ["no", "without"],
            "Extra": ("extra")
        },
        "cream": {
            "None": ["no", "without"],
            "Extra": ("extra")
        }
        
    },
    "random_flavour": {
        "no clue": [
            ("no"),
            ("idea", "think", "clue", "know")
        ],
        "choose for me": [
            ('choos', 'get', 'give', 'pick'),
            ('anyth', 'any', 'random')
        ]
    },
    "unidentified": "Sorry, I don't think we have that flavour! Can you please rephrase your order?",
}
SUPPORTED_COMMAND_PROMPTS = [cmd[1] for cmd in ADMIN_TABLE["commands"]]
CSV_PATH = Path(__file__).parent / "menu.csv"
clear = lambda: os.system('cls')
LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')