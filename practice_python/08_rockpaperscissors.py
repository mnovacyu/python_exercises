import sys

def getInput(player):
    player_input = ""
    player_input = input("%s (R/P/S): " % player)

    while True:
        if player_input == "Q":
            sys.exit()
        elif player_input in moves:
            return player_input
        else:
            print("Input not recognized, please try again.")
            player_input = input("%s (R/P/S): " % player)
            True

def pickWinner(input1, input2):
    if (input1 == input2):
        print("Tie!\n")
    elif ([input1, input2]
            == (["R", "S"]
            or ["S", "P"]
            or ["P", "R"])):
        print("Player 1 Wins!\n")
    else:
        print("Player 2 Wins!\n")

while True:
    moves = ["R", "P", "S"]

    print("New Game!")
    input1 = getInput("Player 1")
    input2 = getInput("Player 2")

    pickWinner(input1, input2)
