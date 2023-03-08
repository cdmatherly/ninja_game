from classes.ninja import Ninja
from classes.pirate import Pirate
import random

name = input("What is your name?\n")

ninja = Ninja(f"{name}")

pirate = Pirate("Jack Sparrow")

print(f"\nWelcome, {name}!\nYou are a ninja.\nA wild pirate appears and looks hostile.\n")

count = 1
recover = 2
smokeCounter = False

while ninja.health > 0 and pirate.health > 0:
    # ninja.quick_attack(pirate)

    if count % 2 != 0:
        response =" "
        response = input("What do you do?\n 1) Normal Attack \n 2) Quick Attack\n 3) Talk\n 4) Heal\n 5) Show Stats\n 6) Run Away\n")
        if response == "1":
            ninja.attack(pirate)
            count += 1
        elif response == "2":
            ninja.quick_attack(pirate)
            count += 1
        elif response == "3":
            num = input(f"\n{pirate.name} says: 'Choose a number between 1 and 3.'\n")
            if num == str(random.randint(1,3)):
                print(f"You chose {num}. Poor decision\n")
                pirate.cannon_ball(ninja)
                count += 1
            else:
                print(f"You chose {num}. Wise decision.\n")
        elif response == "4": 
            if recover > 0:
                ninja.heal()
                recover -= 1
                print(f"Remaining potions: {recover}\n")
                count += 1
            else:
                print(f"You have no more remaining potions\n")
        elif response == "5":
            print(f"Whose stats would you like to see?\n")
            stats = input(f" 1) {ninja.name}'s stats\n 2) {pirate.name}'s stats\n")
            if stats == "1":
                ninja.show_stats()
            elif stats == "2":
                pirate.show_stats()
            else:
                print("Please choose a valid response\n")
        elif response == "6":
            exit = random.randint(1,5)
            if exit == 1:
                print("You successfully got away!")
                quit()
            else:
                print(f"You fool! {pirate.name} caught up to you.\n")
        elif response == "exit":
            quit()
        else:
            print("Choose a valid response\n")
    else:
        hit = random.randint(1,3)
        if pirate.strength != 10:
            pirate.strength = 10
        if hit == 1:
            if smokeCounter:
                pirate.strength += 10
                pirate.attack(ninja)
                count += 1
                smokeCounter = False
            else:    
                pirate.attack(ninja)
                count += 1
        elif hit == 2:
            if smokeCounter:
                pirate.strength += 10
                pirate.cannon_ball(ninja)
                count += 1
                smokeCounter = False
            else:    
                pirate.cannon_ball(ninja)
                count += 1
        elif hit == 3:
            pirate.smoke()
            smokeCounter = True
            count += 1
    if pirate.health <= 0:
        print("You are victorious!\nCongratulations.")
    if ninja.health <= 0:
        print("You have been defeated! Try again, young one.")