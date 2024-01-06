from tictactoe1D import evaluate, move


def test_evaluate_xwinner():
    board = "---xxx--------------"
    assert len(board) == 20
    res = evaluate(board)
    assert res == "x"

def test_evaluate_owinner():
    board = "---ooo--------------"
    assert len(board) == 20
    res = evaluate(board)
    assert res == "o"

def test_evaluate_tie():
    board = "oxxooxooxxoxooxxoxxo"
    assert len(board) == 20
    res = evaluate(board)
    assert res == "!"

def test_evaluate_gamecontinued():
    board = "xoxoxoo-----xoxoxo--"
    res = evaluate(board)
    assert res == "-"

# move tests
def test_move_o():
    board = "--xoxoox--xoxo-xoo-x"
    position = 1
    mark = "o"
    res = move(board, mark, position)
    assert res == "-oxoxoox--xoxo-xoo-x"

def test_move_x():
    board = "--xoxoox--xoxo-xoo-x"
    position = 18
    mark = "x"
    res = move(board, mark, position)
    assert res == "--xoxoox--xoxo-xooxx"

#### a) ####
#A module is a sub-category of a package. It comes with ready-to use code in it.
# A package is a collection of such modules. A code that I have written and stored like tictactoe can be a module
# and I can import it into new code.

#### b) ####
# A side effect is if there is a function that prints something or that asks the user to input something
# steps of the module function should be invisible.

#### c) ####
# Exceptions are error messages. If python cannot run the code - it shows an error message
# This does not necessarily kill the program but can guide the user back to repeat a previous
# step (giving the change of entering a correct input for example.)
# If third-party code throws an exception we can write our code in a way to 
# tell it what to do if an exception is thrown. Like how to proceed. This workd with "except" for example.

#### d) ####
# you can use the keywords: try & except, or else & finally.
# I dont quite understand what is meant by create, throw and catch a custom exception?
    
#### e) ####
# my code can be tested automatically which saves time and can show me bugs, I might not see 
# easily or quickly manually.
# test codes are run automatically and can even send me notifications via email
# if there is a bug in the functionality (regression)
