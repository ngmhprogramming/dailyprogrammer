##create a short text adventure that will call the user by their name. The text adventure should use standard text adventure commands ("l, n, s, e, i, etc.").
##for extra credit, make sure the program doesn't fault, quit, glitch, fail, or loop no matter what is put in, even empty text or spaces. These will be tested
##rigorously!
##For super extra credit, code it in C

from time import sleep
from random import randint

coordinates = [0, 0]
kills = 0
energy = 100
health = 100
attack = 10
enemySpotted = False
enemy = None
enemyHealth = None
enemyAttack = None
enemies = ["Wizard", "Witch", "Goblin", "Skeleton", "Necromancer", "Thief", "Spy", "Bodyguard"]
enemiesHealth = [100, 50, 20, 10, 55, 25, 80, 90]
enemiesAttack = [10, 8, 4, 2, 7, 5, 8, 9]

def move(direction):
    if direction == "w":
        coordinates[1] += 1
    elif direction == "a":
        coordinates[0] -= 1
    elif direction == "s":
        coordinates[1] -= 1
    elif direction == "d":
        coordinates[0] += 1
    enemySpawned = randint(0,1)
    if enemySpawned == 1:
        print("Oh no! An enemy has spawned!")
        enemyIndex = randint(0, len(enemies) - 1)
        global enemySpotted
        global enemy
        global enemyHealth
        global enemyAttack
        enemySpotted = True
        enemy = enemies[enemyIndex]
        enemyHealth = enemiesHealth[enemyIndex]
        enemyAttack = enemiesAttack[enemyIndex]
    else:
        print("Nothing happens.")
        
def fight():
    if enemySpotted:
        print("You are fighting " + enemy + "!")
        global enemyHealth
        global energy
        global health
        global kills
        while enemyHealth > 0:
            print(enemy + " has " + str(enemyHealth) + " health.")
            print("You swing at " + enemy + ".")
            enemyHealth -= attack
            energy -= attack
            sleep(1)
            if energy < 10:
                print("You escape with little energy left.")
                break
            print(enemy + " swings at you.")
            health -= enemyAttack
            sleep(1)
            if health < 1:
                print("You died! No!")
            else:
                print("You have " + str(health) + " health.")
        kills += 1
        print("Good job! You have killed " + enemy + ". You now have " + str(kills) + " kills!")
    else:
        print("There's nobody to fight.")

def rest():
    print("You lie down and rest.")
    sleep(5)
    global energy
    global health
    energy += 10
    health += 10
    if energy > 100:
        energy = 100
    if health > 100:
        health = 100
    print("You feel refreshed, you now have " + str(energy) + " energy and " + str(health) + " health.")

print("Commands: wasd to move, f to fight and r to rest. c for checking coordinates, e for checking energy and h for checking health.")
while True:
    command = input("What do you do? ")
    if command in ["w", "a", "s", "d"]:
        move(command)
    elif command in ["f", "fight"]:
        fight()
    elif command in ["r", "rest"]:
        rest()
    elif command in ["c", "coordinates"]:
        print("You are at " + str(coordinates) + ".")
    elif command in ["e", "energy"]:
        print("You have " + str(energy) + " energy.")
    elif command in ["h", "health"]:
        print("You have " + str(health) +  " health.")
    else:
        print("You stoned.")
