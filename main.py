import random

win = 0
lose = 0
round = 0

while(True):
    sChoise = input("Exit from the game: exit ; Pliz choise: stone, scissors, paper: ")
    iChoise = 0
    bChoise = 0

    if sChoise == "stone":
        iChoise = 1
    elif sChoise == "scissors":
        iChoise = 2
    elif sChoise == "paper":
        iChoise = 3
    else:
        print("Error")
    if iChoise > 0:
        bChoise = random.randint(1, 3)
        if bChoise == 1:
            print("Opponent chose stone")
        if bChoise == 2:
            print("Opponent chose scissors")
        else:
            print("Opponent chose paper")

        if bChoise == iChoise:
            print("No winner")
        elif iChoise == 1 and bChoise == 2:
            win += 1
            round += 1
        elif iChoise == 2 and bChoise == 1:
            lose += 1
            round += 1
        elif iChoise == 1 and bChoise == 3:
            lose += 1
            round += 1
        elif iChoise == 3 and bChoise == 1:
            win += 1
            round += 1
        elif iChoise == 2 and bChoise == 3:
            win += 1
            round += 1
        elif iChoise == 3 and bChoise == 2:
            lose += 1
            round += 1
    if win == 3:
        print("You win")
        lose = 0
        win = 0
    elif lose == 3:
        print("You lose")
        lose = 0
        win = 0
    if round == 3:
        if win > lose:
            print("You win")
            lose = 0
            win = 0
        else:
            print("You lose")
            lose = 0
            win = 0

    print("Wins: ", win, "Lose: ", lose)
    print("")