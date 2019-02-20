class Cell(object):

    def __init__(self, x, y, size, is_alive):
        self.x = x
        self.y = y
        self.is_alive = is_alive
        self.next_state = False
        self.size = size

    # Set values for our next state
    def prepare_next_state(self, board):
        living_neighbors = self.count_living_numbers(board)
        is_alive = self.is_alive

        if is_alive is True:
            if 2 <= living_neighbors <= 3:
                self.next_state = True
            elif living_neighbors < 2:
                self.next_state = False
            elif living_neighbors > 3:
                self.next_state = False
        else:
            if living_neighbors == 3:
                self.next_state = True

    # Enter cell into the next state using the stored values
    def enter_next_state(self):
        self.is_alive = self.next_state
        self.next_state = False

    # Get a list of neighbors to the cell
    def get_all_neighbors(self, board):
        neighbor_list = []
        x = self.x
        y = self.y
        # off-set index by 1 so it matches up
        size = self.size - 1

        # Handle cells to the left
        if not x == 0:
            neighbor_list.append(board[x-1][y])
            # Handle top left corner
            if not y == 0:
                neighbor_list.append(board[x-1][y-1])
            # Handle  bottom left corner
            if not y == size:
                neighbor_list.append(board[x-1][y+1])

        # Handle cells to the right
        if not x == size:
            neighbor_list.append(board[x+1][y])
            # Handle bottom right corner
            if not y == size:
                neighbor_list.append(board[x+1][y+1])
            # Handle top right corner
            if not y == 0:
                neighbor_list.append(board[x+1][y-1])

        # Handle cells above
        if not y == 0:
            neighbor_list.append(board[x][y-1])

        # Handle cells below
        if not y == size:
            neighbor_list.append(board[x][y+1])

        return neighbor_list

    # Find number of living neighbors
    def count_living_numbers(self, board):
        all_neighbors = self.get_all_neighbors(board)
        sum = 0
        for cell in all_neighbors:
            if cell.is_alive:
                sum += 1
        return sum

    # Check if the cell is alvie
    def get_is_alive(self):
        return self.is_alive

    # return string repr of the object
    def __repr__(self):
        if self.is_alive is True:
            return "O"
        else:
            return " "
