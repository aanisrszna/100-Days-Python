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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go ?\nType \"right\" or \"left\"\n").lower()

if choice1 == "left":
    lake= input("Oh we arrive at a lake. There is an island in the middle of the lake."
                "\nType \"wait\" to wait for the boat or \"swim\" to swim to the island\n").lower()
    if lake == "wait":
        color= input("You arrive at island unharmed. There is a house with 3 door. \n One Red, One Blue and One Yellow, which one you choose ?\n").lower()
        if color== "blue":
            print("Eaten by Beast. Game Over!")
        elif color== "red":
            print("Burned by fire. Game Over!")
        elif color == "yellow":
            print("YES YOU WIN!")
        else :
            print("You choose a door that doesnt exist. Game Over")
    else:
        print("Oh No! You got attacked by crocodile. Game Over")

else:
    print("Oh No! You fall into a hole. Game Over")


