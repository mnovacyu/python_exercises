def draw_horizontal(size):
    for x in range(0, size):
        print(" ---", end="")
    print()

def draw_vertical(size):
    for x in range(0, size+1):
        print("|   ", end="")
    print()

def draw_game_board(size):
    for x in range(0, size):
        draw_horizontal(size)
        draw_vertical(size)
    draw_horizontal(size)

while True:
    size = input("What sized game board would you like? ")
    draw_game_board(int(size))
