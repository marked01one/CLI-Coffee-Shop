from pathlib import Path
import os

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
    "random_flavour": [
        ["no", "idea"],
        ['i', 'not', 'know'],
        ['choose', 'choice'],
        ['can', 'not', 'think'],
    ],
    "flavour_choice": {
        "flavour": ["espresso", "cappuccino", "latte"],
        "size": ["small", "medium", "large"],
        "sugar": {
            "None": ["no", "without"],
            "Extra": ["extra"]
        },
        "cream": {
            "None": ["no", "without"],
            "Extra": ["extra"]
        }
        
    },
    "unidentified": "Sorry, I don't think we have that flavour! Can you please rephrase your order?",
}

SUPPORTED_COMMAND_PROMPTS = [cmd[1] for cmd in ADMIN_TABLE["commands"]]

ADMIN_PASSWORD = "billymilly1234"

# ! DO NOT CHANGE THE OPTIONS BELOW !
CSV_PATH = Path(__file__).parent / "menu.csv"
clear = lambda: os.system('cls')