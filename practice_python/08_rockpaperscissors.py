# Simple Rock Paper Scissors game to practice loops and break statements
import sys

# Initialize game
def initGame():
    global moves

    moves = {
        "R": "S",
        "P": "R",
        "S": "R",
        "B": ["R", "P", "S"]}

    print("New Game!")

# Get input from player
def getInput(player):
    player_input = ""
    player_input = input("%s (R/P/S): " % player)

    while True:
        if player_input.upper() == "Q":
            sys.exit()
        elif player_input.upper() in moves:
            return player_input.upper()
        else:
            print("Input not recognized, please try again.")
            player_input = input("%s (R/P/S): " % player)
            True

# Figure out who the winner is
def pickWinner(input1, input2):
    if (input1 == input2):
        print("Tie!\n")
    elif input2 in moves[input1]:
        print("Player 1 Wins!\n")
    else:
        print("Player 2 Wins!\n")

# Get the game going!
while True:
    initGame()

    input1 = getInput("Player 1")
    input2 = getInput("Player 2")

    pickWinner(input1, input2)
