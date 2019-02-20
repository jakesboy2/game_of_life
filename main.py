import Cell
import Board
import sys
import time

# Get the size of the board from the user or the command line
if(len(sys.argv) > 1):
    board_size = int(sys.argv[1])
else:
    board_size = int(input("Enter board size: "))

# Set up the board and draw it on the screen
board = Board.generate_new_board(board_size)
Board.draw_board(board, board_size)

while(True):
    Board.clear_screen()
    Board.draw_board(board, board_size)
    time.sleep(1)
