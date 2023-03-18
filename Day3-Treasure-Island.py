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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

task1 = input("red or blue pill?\n").lower()

if(task1 == "red"):
    
    print("Congratulations! that pill has a secret code for you. Now go on and finish the next task.\n")

    task2 = input("A wild dog has appeared, feed him or scare him?\n").lower()

    if(task2 == "feed him"):
        print("That was a hungry dog who is now in love with you because you fed him, now he takes you to a small cave which has the treasure box!\n")

        task3 = input("There is a box with 2 small compartments , A and B. Which one do you open?\n")

        if(task3 == "B"):
            print("Congratulations! you have found the treasure")
        else:
            print("Compartment A was holding a poisonous gas and it killed you")
    else:
        print("That was a hungry dog, and you irritated him. So he killed you\n")
else:
        print("You are obliterated by a wild polar bear\n")
   
