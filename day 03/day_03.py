print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to The Endless Labyrinth.")
print("Your mission is to find the exit and get your treasure.") 

side = input("You're in a labyrinth and came across two paths, which one do you choose? Left or right?\n")
side = side.lower()
if side == "left":
    print("Great, the path you chose helped you continue forward")

    swim_or_wait = input("Watch out! There is a rock coming towards you, and a river in front of you. What do you do? Swim or wait?\n")
    swim_or_wait = swim_or_wait.lower()
    if swim_or_wait == "wait":
        print("Excellent! For some reason the rock got stuck and you survived!")

        door_color = input("Awesome! You reached the end of the labirynth, but there are three doors. Only one is the correct one. What door do you choose? Red, blue or yellow?\n")
        door_color = door_color.lower()
        if door_color == "yellow":
            print("Amazing! You got out of the labirynth and got the treasure!")
        elif door_color == "blue":
            print("Wrong door! A skeleton with an axe killed you...")
        elif door_color == "red":
            print("Wrong door! A dragon ate you...")
        else:
            print("You died!")
    else:
        print("You died!")
else:
    print("You died!")
