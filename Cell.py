class Cell(object):
    current_x = 0
    current_y = 0
    is_alive = False

    next_x = 0
    next_y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Get values for our next state
    def prepare_next_state(self):
        pass

    # Enter cell into the next state using the stored values
    def enter_next_state(self):
        pass

    # Get a list of neighbors to the cell
    def get_all_neighbors(self):
        pass

    # Find number of living neighbors
    def count_living_numbers(self):
        pass

    # Check if the cell is alvie
    def is_alive(self):
        return self.is_alive

    # return string repr of the object
    def __repr__(self):
        if self.is_alive:
            return "O"
        else:
            return "X"
