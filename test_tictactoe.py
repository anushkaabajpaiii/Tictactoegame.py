from tictactoe import *

# Function to print the board nicely
def print_board(board):
    """ Helper function to print the board nicely """
    for row in board:
        print(row)
    print("\n")

# Test initial state
print("✅ Initial Board:")
board = initial_state()
print_board(board)

# Test player function
print("✅ Next Player:", player(board))

# Test available actions
print("✅ Available Actions:", actions(board))

# Test result function
print("\n✅ Board after X moves at (0, 0):")
new_board = result(board, (0, 0))
print_board(new_board)

# Test winner function with a winning board
winning_board = [[X, X, X],
                 [O, O, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
print("✅ Winner of the test board:", winner(winning_board))

# Test terminal function
print("✅ Is the game over?:", terminal(winning_board))

# Test utility function
print("✅ Utility of the board:", utility(winning_board))

# Test minimax function with an empty board
print("✅ AI (X) chooses move:", minimax(board))
