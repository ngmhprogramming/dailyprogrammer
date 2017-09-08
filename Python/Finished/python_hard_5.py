from random import randint

pirates = []
piratesHealth= []
piratesAttack = []

def evaluateBattle(one, two):
    one = one.lower()
    two = two.lower()
    winner = ["scissors", "paper", "stone"]
    loser = ["paper", "stone", "scissors"]
    if one not in winner or two not in winner:
        return "Again"
    elif loser[winner.index(one)] == two:
        return "Win"
    elif loser[winner.index(two)] == one:
        return "Lose"
    else:
        return "Draw"

def battle():
    global pirates
    global piratesHealth
    global piratesAttack
    
    while True:
        print("Note: Very Buggy.")
        print("Translations from http://funtranslations.com/pirate.")
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
        pirates = []
        piratesHealth = []
        piratesAttack = []

if __name__ == "__main__":
    battle()
