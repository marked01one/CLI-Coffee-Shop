from prettytable import PrettyTable
import time, random, os
clear = lambda: os.system('cls')

class LoadingScreen:
    def __init__(self, loading_line, **islong) -> None:
        if islong:
            self.seconds = random.randint(3,7)
        else:
            self.seconds = random.randint(5,11)
        clear()
        for i in range(self.seconds):
            for k in range(4):
                print(loading_line + "."*k, end="\r")
                time.sleep(0.25)
            clear()
    
class Tables(PrettyTable):
    def __init__(self):
        pass