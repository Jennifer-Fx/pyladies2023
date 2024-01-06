# The ultimate version.6.0 (for the sixth time . fingers crossed)

# First all functions have to be defined to then be integrated into the
# ultimate tictactoesfunciton

from random import randrange

# evaluate (between each player_move and pc_move)
def evaluate(board):
    '''This function checks the board to see if there is a winner, it is a draw
    or the game continues '''
    if "xxx" in board:
        print("You have won. End of game.")
        return "x"
    elif "ooo" in board:
        print("The computer has won. End of game.")
        return "o"
    elif "-" not in board:
        print("It is a tie. End of game.")
        return "!"
    else:
        return "-"

# move (to be integrated in pc_move and player_move)
def move(board, mark, position):
    """ Returns the game board with the given mark in the given position."""
    board = board[:position] + mark + board[position+1:]
    return board

# player_move
def player_move(board):
    while True:
        position = int(input("Enter where you wanna place your mark (choose number between 0-19):"))
        if position < 0 or position > 19:
            print("The entered number is outside the range.")
        elif board[position] == "x" or board[position] == "o":
            print("This space on the board is already occupied. Try again.")
        else:
            break
    mark = "x"
    return move(board, mark, position)


# pc_move
def pc_move(board):
    """Returns a game board with the computer's move. Let's the pc draw a random
    number until the random number fits a position which is still empty."""
    while True:
        position = randrange(0,19)
        if board[position] == "-":
            break
    mark = "o"
    return move(board, mark, position)


# the final function with the usage of all functions from above

def tictactoe():
    game_on = input("Hello, do you care to play a game of Tic Tac Toe with me?\nEnter yes or no: ")
    if game_on == "no":
        print("Alright, maybe another time.")
    else:
        print("Hurray, let's get started.")
        board = "--------------------"
        while True:
            print(board) # prints board before each move so you can see what to choose
            evaluate_return_value = evaluate(board) 
            if evaluate_return_value != "-":
                print(board) # if the game ends you still wanna see the last move and how the board looks
                break
            board = player_move(board)
            evaluate_return_value = evaluate(board)
            if evaluate_return_value != "-":
                print(board)
                break
            board = pc_move(board)


