import random

def Clean():
    global wins, defeats, rounds
    wins = 0
    defeats = 0
    rounds = 0

def Compare(a, b):
    global wins, defeats, rounds
    if a == b:
        print("\n" * 10, "                                No winner")
    elif (a == 1 and b == 2) or (a == 3 and b == 1) or (a == 2 and b == 3):
        print("\n" * 10, "                                You win")
        wins += 1
        rounds += 1
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("\n" * 10, "                                You lose")
        defeats += 1
        rounds += 1

def IntToString(a):
    return option[a]

option = {1 : "Rock", 2 : "Scissors", 3 : "Paper"}
wins = 0
defeats = 0
rounds = 0

while True:
    PlayerChoiseInt = int(input("Rock = 1; Scissors = 2; Paper = 3 : "))
    OtherChoiseInt = random.randint(1, 3)
    Compare(PlayerChoiseInt, OtherChoiseInt)
    try:
        print("(rounds): ", rounds, " (wins): ", wins, " (defeats): ", defeats, " (Player choise): ", IntToString(PlayerChoiseInt), " (Other choise): ", IntToString(OtherChoiseInt), "\n\n\n")
    except BaseException:
        print("\n" * 15, "Try again pliz")
        continue
    if rounds == 3 and wins > defeats:
        print("\n" * 10 ,"            ---------------You have won this game!---------------\n")
        Clean()
        continue
    elif rounds == 3 and wins < defeats:
        print("\n" * 10 ,"            ---------------You lost in this game!---------------\n")
        Clean()
        continue