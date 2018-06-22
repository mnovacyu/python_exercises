# Simple board game drawing script
def draw_horizontal(size):
    print(" ---" * size)

def draw_vertical(size):
    print("|   " * (size+1))

def draw_game_board(size):
    for x in range(0, size):
        draw_horizontal(size)
        draw_vertical(size)
    draw_horizontal(size) # close off the board

while True:
    size = input("What sized game board would you like? ")
    draw_game_board(int(size))
