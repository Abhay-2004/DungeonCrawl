
# Abhay Prasanna Rao



import random
import sys


# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 9999

#Combat function

def combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health):
    print("You have engaged in combat")
    print(f"You have encountered a crazy {monster_name}")
    while monster_health>0 and player_health>0:
            choice= input("COMBAT: (a)ttack, (f)lee: ")
            if choice=="a":
                if defeatedIris==True:
                    print(f"You slash the {monster_name} with your sword and deal {player_dmg} damage")
                    monster_health-=player_dmg
                    print(f"monster health = {monster_health}")
                    print()
                else:
                    hitOrMiss= random.randint(0,1)
                    if hitOrMiss== 0:
                        print(f"You tried to stab the {monster_name} but it dodged your attack")
                        print(f"monster health = {monster_health}")
                        print()
                    else:
                        print(f"You slash the {monster_name} with your sword and deal {player_dmg} damage")
                        monster_health-=player_dmg
                        print(f"monster health = {monster_health}")
                        print()
            elif choice=="f":
                currentRoom=1
                print(f"You succesfully fled to room{currentRoom} (Hint: try exploring a different room, you might find resources to make you stronger)")
                break           
            if monster_health<=0:
                print(f"You succesfully defeated the {monster_name}!")
                print()
            else:
                hitOrMiss= random.randint(0,1)
                if hitOrMiss==0:
                    print(f"The {monster_name} tried to bite you but you dodged the attack")
                    print()
                else:
                    print(f"The {monster_name} bit you for {monster_dmg} damage")
                    player_health-=monster_dmg
                    print(f"player current health = {player_health}/{player_total_health}")
                    print()
                    if player_health<=0:
                        print(f"You were slayed by the wild {monster_name} and perished in the dungeon of doom. (Hint: try exploring a different room, you might find resources to make you stronger)")
                        print(" ________________________________________________")
                        print("|    G    A    M    E        O    V    E    R    |")
                        print(" IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
                        print()

                        gameOver = True
                        
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health


#Shop function

def shop(goldAmount, player_health, player_dmg, player_total_health):
    choice="z"
    while choice!="c":
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f'''\nThe magical realm   (Current gold = {goldAmount})
            a) Mango milkshake (gives you max health) = 20 gold
            b) Starbucks drink (Enhances your damage by 1) = 15 gold
            c) Exit the magical realm
            ''')
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        choice= input("Enter (a), (b) or (c) : ")   
        if choice=="a":
            if goldAmount<20:
                print("You need more gold! Go and grab some and come back! ")
            else:
                player_health= player_total_health
                goldAmount-=20
                print(f"Purchase completed! Go and slay the deamons now.....HAHAHAH! ")
                print()
        elif choice=="b":
            if goldAmount<15:
                print("You need more gold! Go and grab some and come back!")
            else:
                player_dmg+=1
                goldAmount-=15
                print(f"Purchase completed! Go and slay the deamons now.....HAHAHAH! ")
                print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return goldAmount, player_health, player_dmg, player_total_health

# 1st room

def room1(goldAmount, visited_room, currentRoom):

    if visited_room == False:
        
        gold = 15 
        print()
        print("Hi There, I am the ghost speaking with you. You have come to me, i will reward you with gold! Enjoy and come again, I am very lonely")
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("(This is the Start Room) You have already visited it before...")
        print()
    print("Where do you wish to travel? ")
    direction = input("[n] [s] [e] [w]?: ")
    while direction != "n" and direction != "e" and direction != "w" and direction !="s":
        print("Error! Invalid input...")
        direction = input("[n] [s] [e] [w]?: ")
    if direction=="n":
        currentRoom=4
    if direction=="w":
        currentRoom=2
    if direction=="e":
        currentRoom=3
    if direction =="s":
        currentRoom = 6
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return goldAmount, visited_room, currentRoom

# 2nd room

def room2(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health):
    gold = 20 
    monster_health=3
    monster_dmg=1
    monster_name="Vampire"
    if visited_room == False:
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health)
        if gameOver== True:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        if currentRoom !=2:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        else:
            print()
            print("The room has", gold, "gold pieces in it...")
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
        visited_room= True
    else:
        print()
        print("You have already visited this room before...(this is the west side vampire room)")
        print()
    entershop=input("Enter magical realm ? (y),(n)")
    if entershop=="y":
        goldAmount, player_health, player_dmg, player_total_health= shop(goldAmount, player_health, player_dmg, player_total_health)
    print("where do you want to go?")
    direction = input("[e]?: ")
    while direction != "e":
        print("Invalid input...")
        direction = input("[e]?: ")
    if direction=="e":
        currentRoom=1
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health

# 3rd room
def room3(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health):
    gold=10
    monster_health=3
    monster_dmg=2
    monster_name="Iris"
    if visited_room == False:
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health)
        if gameOver== True:
            currentRoom=1
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        if currentRoom !=3:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        else:
            print("You have defeated Iris and gained the \"Eye Of Iris\". You have conquored the deamon slayer")
            defeatedIris=True
            print("The room has", gold, "gold pieces in it...")
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
        visited_room= True
    else:
        print()
        print("You have already visited this room before...(this is the east side Iris room)")
        print()

    print("where do you wish to travel?")
    direction = input("[w]?: ")
    while direction != "w":
        print("Error! Invalid input...")
        direction = input("[w]?: ")
 
    if direction=="w":
        currentRoom=1
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health


# 4th room

def room4(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health):
    gold = 5 
    monster_health=3
    monster_dmg=1
    monster_name="Dracula"
    if visited_room == False:
        print("You can feel that the exit is nearby. You feel a strange aura coming from the north")
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health)
        if gameOver== True:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        if currentRoom !=4:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        else:
            print()
            print("The room has", gold, "gold pieces in it...")
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
        visited_room= True
    else:
        print()
        print("You have already visited this room before...(this is the north side Dracula room)")
        print()
    entershop=input("Enter the magical Realm? (y),(n)")
    if entershop=="y":
        goldAmount, player_health, player_dmg, player_total_health= shop(goldAmount, player_health, player_dmg, player_total_health)
    print("where do you want to go?")
    print("Hint : Select n to visit the final room! ")
    direction = input("[n],[s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n],[s]?: ")
 
    if direction=="n":
        currentRoom=5
    else:
        currentRoom=6
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health

#( FINAL_ROOM function) 5th room

def room5(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health):
    gold=1000
    monster_health=6
    monster_dmg=2
    monster_name=" Boss Zombie"
    if visited_room == False:
        print("Your heart beat is rising, it corssed 200 beats per minute, The light is flickering. You hear the walls vibrating, you walk and wake the creature, here he comes running, screaming, HEEEEE!.")
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health)
        if gameOver== True:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        if currentRoom !=5:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        else:
            print("You defeated the dungeon boss and are free to leave! ")
            print("The treasure box in this room has 0 gold pieces in it...instead, it has a huge elixer worth 1000 gold!")
            goldAmount += gold
            print()
        visited_room= True
        print(visited_room)
    else:
        print()
        print("You have already visited this room before...(this is the north side Boss Zombie room)")
        print()
    print("where do you want to go? ((n)orth to exit dungeon, (s)outh to keep exploring)")
    direction = input("[n],[s]?: ")

    while direction != "n" and direction != "s":
        print(" Error! Invalid input...")
        direction = input("[n],[s]?: ")
 
    if direction=="n":
        print("You have exited the dungeon! ALL HAIL THE LORD! ")
        currentRoom=FINAL_ROOM
    else:
        currentRoom=4
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health

# Room 6 ( Not the final room, Final Room is defined as room5)

def room6(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health):
    gold=50
    monster_health=4
    monster_dmg=1
    monster_name="Warewolf"
    if visited_room == False:
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom, monster_name, gameOver, defeatedIris, player_total_health)
        if gameOver== True:
            currentRoom=5
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        if currentRoom !=6:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health
        else:
            print("You have defeated the Alpha of the warewolf. You have conquored this monster.")
            defeatedIris=True
            print("The room has", gold, "gold pieces in it...")
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
        visited_room= True
    else:
        print()
        print("Suprise is coming...You are time travelling! ")
        print("You have already visited this room before...(this is the east side warewolf room)")
        print()

    print("where do you wish to travel?")
    direction = input("[w]?: ")
    while direction != "w":
        print("Error! Invalid input...")
        direction = input("[w]?: ")
 
    if direction=="w":
        currentRoom=4
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedIris, player_total_health

# Main function
def main():
    gameOver = False

    START_GOLD = 0 
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False
    visited_room2 = False
    visited_room3 = False
    visited_room4 = False
    visited_room5 = False
    visited_room6 = False
    defeatedIris = False
    player_total_health = 10
    player_health = 10
    player_dmg = 1
    

    print("Welcome to Dungeon Crawl...You life is in your hands! YEEEEEET")
    print()
    print("\nBy: Abhay Prasanna Rao")
    print()

    while True:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p":
            print("Your courage and need for the gold has lead you here. What will be your fate in the rooms beyond?")
            while gameOver==False:
                if currentRoom == 1:
                    goldAmount, visited_room1, currentRoom = room1(goldAmount, visited_room1, currentRoom)
                elif currentRoom == 2:
                        currentRoom, goldAmount, visited_room2, player_health, player_dmg, gameOver, defeatedIris, player_total_health = room2(currentRoom, goldAmount, visited_room2, player_health, player_dmg, gameOver, defeatedIris, player_total_health)
                elif currentRoom == 3:
                    currentRoom, goldAmount, visited_room3, player_health, player_dmg, gameOver, defeatedIris, player_total_health= room3(currentRoom, goldAmount, visited_room3,  player_health, player_dmg, gameOver, defeatedIris, player_total_health)
                elif currentRoom == 4:
                    currentRoom, goldAmount, visited_room4, player_health, player_dmg, gameOver, defeatedIris, player_total_health = room4(currentRoom, goldAmount, visited_room4,  player_health, player_dmg, gameOver, defeatedIris, player_total_health)
                elif currentRoom == 5:
                    currentRoom, goldAmount, visited_room5, player_health, player_dmg, gameOver, defeatedIris, player_total_health = room5(currentRoom, goldAmount, visited_room5,  player_health, player_dmg, gameOver, defeatedIris, player_total_health)
                elif currentRoom ==6:
                    currentRoom, goldAmount, visited_room6, player_health, player_dmg, gameOver, defeatedIris, player_total_health = room6(currentRoom, goldAmount, visited_room6,  player_health, player_dmg, gameOver, defeatedIris, player_total_health)

                elif currentRoom == FINAL_ROOM:
                    print()
                    print("You have escaped with", goldAmount, "gold from the dungeon!")
                    print(" ________________________________________________")
                    print("|    G    A    M    E        O    V    E    R    |")
                    print(" IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
                    print()

                    print()
                    gameOver=True
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()

            goldAmount = START_GOLD
            currentRoom = START_ROOM
            visited_room1 = False
            visited_room2 = False
            visited_room3 = False
            visited_room4 = False
            visited_room5 = False
            visited_room6 = False
            defeatedIris = False
            player_total_health = 10
            player_health = 10
            player_dmg = 1
            gameOver=False
        elif choice == "i": 
            print("Here are the magical instructions! HAHAHAH \n")
            print('''Do you want to know how to explore and move around, take a look at the below options! 
                    n= north
                    s= south
                    e= east
                    w= west''')
            print('Want to beat the monsters and become the conquorer, then collect gold, explore different rooms, buy portions from the magical realm! \n')

        elif choice == "q": 
            gameOver = True
            print("Goodbye!")
            exit()
    
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()