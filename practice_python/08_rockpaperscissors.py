# Simple Rock Paper Scissors game to practice loops and break statements
import sys

def initGame():
    global moves

    moves = {
        "R": "S",
        "P": "R",
        "S": "R",
        "B": ["R", "P", "S"]}

    print("New Game!")

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
    elif input2 in moves[input1]:
        print("Player 1 Wins!\n")
    else:
        print("Player 2 Wins!\n")

# Get the game going
while True:
    initGame()

    input1 = getInput("Player 1")
    input2 = getInput("Player 2")

    pickWinner(input1, input2)
