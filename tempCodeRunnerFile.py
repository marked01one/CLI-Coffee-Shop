menu_table = PrettyTable()
with open("[Python] CLI Coffee Shop/menu.csv") as menu_csv:
    menu_table = from_csv(menu_csv)