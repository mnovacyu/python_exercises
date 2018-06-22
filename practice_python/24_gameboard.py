# Simple board game drawing script
def draw_horizontal(size):
    print(" ---" * size)

def draw_vertical(size):
    print("|   " * (size+1))

def draw_game_board(length, height):
    for x in range(height):
        draw_horizontal(length)
        draw_vertical(length)
    draw_horizontal(length) # close off the board

while True:
    length = int(input("What length would you like? "))
    height = int(input("What height would you like? "))
    draw_game_board(length, height)
