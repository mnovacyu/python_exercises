# script checks for winners of a tic tac toe game
# is built to scale for bigger boards and more players

# find out if there is a winner from a list, where all elements need to match
def is_there_a_winner(list):
    if len(set(list)) == 1:
        return list[0]
    else:
        return 0

# returns a row winner
def row_winner(board, row):
    return is_there_a_winner(board[row])

# returns a column winner
def column_winner(board, column):
    list = []
    for x in range(len(board)):
        list.append(board[x][column])
    return is_there_a_winner(list)

# returns a *list* of diagonal winners
def diag_winner(board):
    list = []
    diag1 = []
    diag2 = []
    for x in range(len(board)):
        diag1.append(board[x][x])
        diag2.append(board[x][len(board)-1-x])
    list.append(is_there_a_winner(diag1))
    list.append(is_there_a_winner(diag2))
    return list

# returns the true winner(s)
def find_winner(board):
    row_list = []
    column_list = []
    for x in range(len(board)):
        row_list.append(row_winner(board, x))
        column_list.append(column_winner(board, x))
    diag_list = diag_winner(board)
    full_winner_list = [row_list, column_list, diag_list]
    shortened_list = set([y for x in full_winner_list for y in x if y!=0])
    if len(shortened_list) == 0:
        shortened_list = {0}
    return [row_list, column_list, diag_list, shortened_list]

def print_winners(board):
    winner = find_winner(board)
    print("%s - Row Winners" % winner[0])
    print("%s - Column Winners" % winner[1])
    print("%s - Diagonal Winners" % winner[2])
    print("%s - Final Winner(s) List" % winner[3])

# samples
winner_is_1 = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [
    [0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

bigger_sample = [
    [1, 2, 3, 4],
	[4, 4, 4, 4],
	[2, 4, 1, 4],
    [4, 3, 2, 4]]

# find and print out winner(s)
print_winners(bigger_sample)
