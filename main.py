import random

def comparison(a, b, c, g, f):
    c = 0
    g = 0
    f = 0
    
    if a == b:
        print("\n", "                                No winner")
        return c, g, f
    elif a == 1 and b == 2:
        print("\n", "                                You win")
        c += 1
        f += 0
        g += 1
        return c, g, f
    elif a == 1 and b == 3:
        print("\n", "                                You defeat")
        c += 1
        g += 0
        f += 1
        return c, g, f
    elif a == 3 and b == 1:
        print("\n", "                                You win")
        c += 1
        g += 1
        f += 0
        return c, g, f
    elif a == 2 and b == 3:
        print("\n", "                                You win")
        c += 1
        f += 0
        g += 1
        return c, g, f
    elif a == 2 and b == 1:
        print("\n", "                                You defeat")
        c += 1
        f += 1
        g += 0
        return c, g, f
    elif a == 3 and b == 2:
        print("\n", "                                You defeat")
        c += 1
        g += 0
        f += 1
        return c, g, f

def IntToString(a):
    return option[a-1]

option = ["Stone", "Scissors", "Paper"]
wins = 0
defeats = 0
round = 0

while True:
    PlayerChoiseInt = int(input("Stone = 1; Scissors = 2; Paper = 3 : "))
    OtherChoiseInt = random.randint(1, 3)
    if 0 > PlayerChoiseInt or 4 < PlayerChoiseInt:
        print("Error")
        continue
    PlayerChoiseStr = IntToString(PlayerChoiseInt)
    OtherChoiseStr = IntToString(OtherChoiseInt)
    r, w, d = comparison(PlayerChoiseInt, OtherChoiseInt, round, wins, defeats)
    round += r
    wins += w
    defeats += d
    print("(rounds): ", round, " (wins): ", wins, " (defeats): ", defeats, " (Player choise): ", PlayerChoiseStr, " (Other choise): ", OtherChoiseStr, "\n")
    if round == 3 and wins > defeats:
        print("            ---------------You have won this game!---------------\n")
        wins = 0
        defeats = 0
        round = 0
        continue
    elif round == 3 and wins < defeats:
        print("            ---------------You lost in this game!---------------\n")
        wins = 0
        defeats = 0
        round = 0
        continue