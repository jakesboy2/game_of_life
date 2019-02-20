import Cell
import Board
import sys

# Get the size of the board from the user or the command line
if(len(sys.argv) > 1):
    board_size = sys.argv[1]
else:
    board_size = input("Enter board size: ")
