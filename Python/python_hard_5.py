##Arrr, me mateys! Yer' challenge fer' today be a tough one. It be gettin awfully borein' on the high seas, so yer' job be to create a pirate based fightin' game! This game oughter' be turn based, and you oughter' be able to pick yer attacks every turn. The best game'll be winnin' some custom flair, and all the rest o' ya will be walkin the plank!
##Translations from http://funtranslations.com/pirate

from random import randint

pirates = []
piratesHealth= []
piratesAttack = []

def evaluateBattle(one, two):
    winner = ["Scissors", "Paper", "Stone"]
    loser = ["Paper", "Stone", "Scissors"]
    if one not in winner or two not in winner:
        return "Again"
    elif loser[winner.index(one)] == two:
        return "Win"
    elif loser[winner.index(two)] == one:
        return "Lose"
    else:
        return "Draw"

while True:
    number = input("How many players? ")
    for player in range(int(number)):
        name = input("Player " + str(player + 1) + "\'s name? ")
        health = input("Player " + str(player + 1) + "\'s health? ")
        attackMin = input("Player " + str(player + 1) + "\'s minimum attack? ")
        attackMax = input("Player " + str(player + 1) + "\'s maximum attack? ")
        pirates.append(name)
        piratesHealth.append(int(health))
        piratesAttack.append([int(attackMin), int(attackMax)])
    print("Let's begin!")
    currentPlayer = 0
    while len(pirates) > 1:
        if piratesHealth[currentPlayer] < 1:
            pirates.pop(currentPlayer)
            piratesHealth.pop(currentPlayer)
            piratesAttack.pop(currentPlayer)
            currentPlayer += 1
        if currentPlayer > (len(pirates) - 1):
            currentPlayer = 0
        if len(pirates) == 1:
            break
        target = input("Player " + str(currentPlayer + 1) + ", who do ye want \'t attack? Check \'t check health. ")
        if target == "check":
            print(", ".join(pirates) + " have " + ", ".join(str(pirate) for pirate in piratesHealth) + " health respectively.")
        else:
            attackerSign = input("Player " + str(currentPlayer + 1) + ", Scissors, Paper, or Stone? ")
            targetSign = input("Player " + str(pirates.index(target) + 1) + ", Scissors, Paper, or Stone? ")
            result = evaluateBattle(attackerSign, targetSign)
            if result == "Win":
                damage = randint(piratesAttack[currentPlayer][0], piratesAttack[currentPlayer][1])
                piratesHealth[pirates.index(target)] -= damage
                print("Aye, avast! " + target + " be left with " + str(piratesHealth[pirates.index(target)]) + " health!")
                currentPlayer += 1
            elif result == "Lose":
                damage = randint(piratesAttack[pirates.index(target)][0], piratesAttack[pirates.index(target)][1])
                piratesHealth[currentPlayer] -= damage
                print("Nay, by Blackbeard's sword! Ye be left with " + str(piratesHealth[currentPlayer]) + " health!")
                currentPlayer += 1
            elif result == "Draw":
                print("Nobody gets hurt!")
                currentPlayer += 1
            elif result == "Again":
                print("Try again!")
    print(pirates[0] + " be th\' winner!")
