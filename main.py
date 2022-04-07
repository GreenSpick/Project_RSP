import random

def cleaning():
    global wins, defeats, round
    wins = 0
    defeats = 0
    round = 0

def comparison(a, b):
    global wins, defeats, round
    if a == b:
        print("\n" * 10, "                                No winner")
    elif (a == 1 and b == 2) or (a == 3 and b == 1) or (a == 2 and b == 3):
        print("\n" * 10, "                                You win")
        wins += 1
        round += 1
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("\n" * 10, "                                You lose")
        defeats += 1
        round += 1

def IntToString(a):
    return option[a-1]

option = ["Rock", "Scissors", "Paper"]
wins = 0
defeats = 0
round = 0

while True:
    PlayerChoiseInt = int(input("Rock = 1; Scissors = 2; Paper = 3 : "))
    OtherChoiseInt = random.randint(1, 3)
    comparison(PlayerChoiseInt, OtherChoiseInt)
    print("(rounds): ", round, " (wins): ", wins, " (defeats): ", defeats, " (Player choise): ", IntToString(PlayerChoiseInt), " (Other choise): ", IntToString(OtherChoiseInt), "\n\n\n")

    if round == 3 and wins > defeats:
        print("\n" * 10 ,"            ---------------You have won this game!---------------\n")
        cleaning()
        continue
    elif round == 3 and wins < defeats:
        print("\n" * 10 ,"            ---------------You lost in this game!---------------\n")
        cleaning()
        continue