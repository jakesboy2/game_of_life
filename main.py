import Cell
import Board
import sys
import time


# Loop over the board and get the next state for each cell
def get_next_states(board, size):
    for col in range(size):
        for row in range(size):
            board[col][row].prepare_next_state()


# Loop over the board and apply for the next state for each cell
def apply_next_states(board, size):
    for col in range(size):
        for row in range(size):
            board[col][row].enter_next_state()


def main():

    # Coords are board[y][x]
    # Get the size of the board from the user or the command line
    if(len(sys.argv) == 2):
        board_size = int(sys.argv[1])
        generation_time = int(input("Enter generation speed: "))
    elif(len(sys.argv) == 3):
        print(sys.argv)
        board_size = int(sys.argv[1])
        generation_time = int(sys.argv[2])
    else:
        board_size = int(input("Enter board size: "))
        generation_time = int(input("Enter generation speed: "))

    # Set up the board and draw it on the screen
    board = Board.generate_new_board(board_size)
    Board.draw_board(board, board_size)

    while(True):

        # Clear screen of last generation
        Board.clear_screen()

        # Pre-update next state
        get_next_states(board, board_size)
        # Apply next state update
        apply_next_states(board, board_size)

        # Draw the new board and wait for next generation
        Board.draw_board(board, board_size)
        time.sleep(generation_time)


if __name__ == '__main__':
    main()
