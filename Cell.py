class Cell(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = False
        self.next_state = False

    # Get values for our next state
    def prepare_next_state(self):
        self.next_state = True

    # Enter cell into the next state using the stored values
    def enter_next_state(self):
        self.is_alive = self.next_state
        self.next_state = False

    # Get a list of neighbors to the cell
    def get_all_neighbors(self):
        pass

    # Find number of living neighbors
    def count_living_numbers(self):
        pass

    # Check if the cell is alvie
    def get_is_alive(self):
        return self.is_alive

    # return string repr of the object
    def __repr__(self):
        if self.is_alive is True:
            return "O"
        else:
            return "X"
