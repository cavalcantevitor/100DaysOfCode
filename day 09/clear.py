import os
     
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
