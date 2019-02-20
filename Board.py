import Cell
import os


# Draw the board that we are provided
def draw_board(board, size):
    printing_string = ""
    for col in range(size):
        for row in range(size):
            printing_string += str(board[col][row])
            printing_string += "  "
        printing_string += '\n'
    print(printing_string)


# Clear the console screen
def clear_screen():
    os.system('clear')


# Return a 2d array full of dead cells
def generate_new_board(size):
    board = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append(Cell.Cell(x, y))
        board.append(row)
    return board

