"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""


# import poc_fifteen_gui


# noinspection PyMethodMayBeStatic,PyUnreachableCode
class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        # create the grid
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid is not None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        # [0, 1, 2, 3]
        # [4, 5, 6, 7]
        # [8, 9, 10, 11]
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return row, col
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                # if key is l move me one col left
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                # assign me to be 0 after moving to the left
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    def solved_board(self):
        solved = [[col + self._width * row
                   for col in range(self._width)]
                  for row in range(self._height)]
        return solved

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # replace with your code
        assert self._grid[target_row][target_col] is not None
        board_copy = self.solved_board()
        zero_row, zero_col = self.current_position(0, 0)  # get the current position of 0th tile
        if zero_row != target_row:
            return False
        if zero_col != target_col:
            return False

        values_after_zerotile = self._grid[zero_row][1 + zero_col:]
        solved_values_after_zerotile = board_copy[zero_row][1 + zero_col:]
        for row in range(1, self._height - target_row):  # restrict search to only rows >= target_row
            values_after_zerotile += self._grid[zero_row + row]
            solved_values_after_zerotile += board_copy[zero_row + row]
        return values_after_zerotile == solved_values_after_zerotile

    def position_helper_interior(self, target_row, target_col):
        board_copy = self.solved_board()

        target_current_row, target_current_col = self.current_position(target_row, target_col)
        all_moves = ""
        # if the target tile is above me
        # step 1: get to the row
        # step 2: do the cyclic motion and bring it my position
        # step 3: place myself at (target_row, target_col - 1)
        if target_current_row < target_row:
            all_moves += 'u' * (target_row - target_current_row)
            self.update_puzzle('u' * (target_row - target_current_row))

            # if the target tile is above me but to the left
            if target_current_col < target_col:
                # go left (target_col - target_current_col) times
                all_moves += 'l' * (target_col - target_current_col)
                self.update_puzzle('l' * (target_col - target_current_col))
                _, target_current_col = self.current_position(target_row, target_col)
                # drrul (target_col - target_current_col) times
                # move it right above target_col
                all_moves += 'drrul' * (target_col - target_current_col)
                self.update_puzzle('drrul' * (target_col - target_current_col))
                all_moves += 'drul'
                self.update_puzzle('drul')
                target_current_row, _ = self.current_position(target_row, target_col)
                # then go ddrul (target_current_row - target_row) times
                all_moves += 'ddrul' * (target_row - target_current_row)
                self.update_puzzle('ddrul' * (target_row - target_current_row))
                # then go left and down once
                all_moves += 'd'
                self.update_puzzle('d')

            # if the target_tile is directly above me
            elif target_current_col == target_col:
                # then go one column left
                all_moves += 'l'
                self.update_puzzle('l')
                # what is the current position of the tile that is supposed to be at
                # target_row, target_col
                target_current_row, _ = self.current_position(target_row, target_col)
                # then go ddrul (target_current_row - target_row) times
                all_moves += 'ddrul' * (target_row - target_current_row)
                self.update_puzzle('ddrul' * (target_row - target_current_row))
                # then go left and down once
                all_moves += 'd'
                self.update_puzzle('d')

            # if the target tile is above me but to the right
            elif target_current_col > target_col:
                all_moves += 'r' * (target_current_col - target_col)
                self.update_puzzle('r' * (target_current_col - target_col))
                _, target_current_col = self.current_position(target_row, target_col)
                all_moves += 'dllur' * (target_current_col - target_col)
                self.update_puzzle('dllur' * (target_current_col - target_col))
                all_moves += 'dlul'
                self.update_puzzle('dlul')
                target_current_row, _ = self.current_position(target_row, target_col)
                all_moves += 'ddrul' * (target_row - target_current_row)
                self.update_puzzle('ddrul' * (target_row - target_current_row))
                all_moves += 'd'
                self.update_puzzle('d')

        elif target_current_row == target_row:
            if target_col - target_current_col == 1:
                all_moves += 'l'
                # if it is just one column left then just move one left
                self.update_puzzle('l')
            elif target_col - target_current_col > 1:
                _, target_current_col = self.current_position(target_row, target_col)
                # ll urrdl
                # left * (target_col - target_current_col)
                all_moves += 'l' * (target_col - target_current_col)
                self.update_puzzle('l' * (target_col - target_current_col))
                _, target_current_col = self.current_position(target_row, target_col)
                all_moves += 'urrdl' * (target_col - target_current_col)
                self.update_puzzle('urrdl' * (target_col - target_current_col))

        return all_moves


    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        target_current_row, target_current_col = self.current_position(target_row, target_col)
        assert self.lower_row_invariant(target_row, target_col) is True
        assert target_row > 1 and target_col > 0
        if target_current_row == target_row:
            assert target_current_col < target_col
        else:
            assert target_current_row < target_row

        all_moves = ""
        # if the target tile is above me
        # step 1: get to the row
        # step 2: do the cyclic motion and bring it my position
        # step 3: place myself at (target_row, target_col - 1)
        if target_current_row < target_row:
            all_moves += 'u' * (target_row - target_current_row)
            self.update_puzzle('u' * (target_row - target_current_row))

            # if the target tile is above me but to the left
            if target_current_col < target_col:
                # go left (target_col - target_current_col) times
                all_moves += 'l' * (target_col - target_current_col)
                self.update_puzzle('l' * (target_col - target_current_col))
                _, target_current_col = self.current_position(target_row, target_col)
                # drrul (target_col - target_current_col) times
                # move it right above target_col
                all_moves += 'drrul' * (target_col - target_current_col)
                self.update_puzzle('drrul' * (target_col - target_current_col))
                all_moves += 'drul'
                self.update_puzzle('drul')
                target_current_row, _ = self.current_position(target_row, target_col)
                # then go ddrul (target_current_row - target_row) times
                all_moves += 'ddrul' * (target_row - target_current_row)
                self.update_puzzle('ddrul' * (target_row - target_current_row))
                # then go left and down once
                all_moves += 'd'
                self.update_puzzle('d')

            # if the target_tile is directly above me
            elif target_current_col == target_col:
                # then go one column left
                all_moves += 'l'
                self.update_puzzle('l')
                # what is the current position of the tile that is supposed to be at
                # target_row, target_col
                target_current_row, _ = self.current_position(target_row, target_col)
                # then go ddrul (target_current_row - target_row) times
                all_moves += 'ddrul' * (target_row - target_current_row)
                self.update_puzzle('ddrul' * (target_row - target_current_row))
                # then go left and down once
                all_moves += 'd'
                self.update_puzzle('d')

            # if the target tile is above me but to the right
            elif target_current_col > target_col:
                all_moves += 'r' * (target_current_col - target_col)
                self.update_puzzle('r' * (target_current_col - target_col))
                _, target_current_col = self.current_position(target_row, target_col)
                all_moves += 'dllur' * (target_current_col - target_col)
                self.update_puzzle('dllur' * (target_current_col - target_col))
                all_moves += 'dlul'
                self.update_puzzle('dlul')
                target_current_row, _ = self.current_position(target_row, target_col)
                all_moves += 'ddrul' * (target_row - target_current_row)
                self.update_puzzle('ddrul' * (target_row - target_current_row))
                all_moves += 'd'
                self.update_puzzle('d')

        elif target_current_row == target_row:
            if target_col - target_current_col == 1:
                all_moves += 'l'
                # if it is just one column left then just move one left
                self.update_puzzle('l')
            elif target_col - target_current_col > 1:
                _, target_current_col = self.current_position(target_row, target_col)
                # ll urrdl
                # left * (target_col - target_current_col)
                all_moves += 'l' * (target_col - target_current_col)
                self.update_puzzle('l' * (target_col - target_current_col))
                _, target_current_col = self.current_position(target_row, target_col)
                all_moves += 'urrdl' * (target_col - target_current_col)
                self.update_puzzle('urrdl' * (target_col - target_current_col))

        assert self.lower_row_invariant(target_row, target_col - 1) is True
        return all_moves

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # assert target_row > 1
        assert self.lower_row_invariant(target_row, 0)
        all_moves = 'ur'
        self.update_puzzle('ur')
        # LUCKY CASE when just 'ur' solves the problem
        if self.current_position(target_row, 0) == (target_row, 0):
            zero_row, zero_col = self.current_position(0, 0)
            all_moves += 'r' * (self._width - 1 - zero_col)
            self.update_puzzle('r' * (self._width - 1 - zero_col))
        elif self.current_position(target_row, 0) != (target_row, 0):
            # position the target tile to (i-1, 1)
            zero_row, zero_col = self.current_position(0, 0)
            # all_moves += 'u' * (self._height - zero_row)
            # self.update_puzzle('u' * (self._height - zero_row))
            # all_moves += 'l'
            # self.update_puzzle('l')
            zero_row, zero_col = self.current_position(0, 0)
            # position the zero tile to (i-1, 0) with solve_interior_tile
            # all_moves += 'druld' * (self._height - 2 - zero_row)
            # self.update_puzzle('druld' * (self._height - 2 - zero_row))
            print(self)
            print(zero_row, zero_col)
            self.position_helper_interior(3, 0)
            print("BOSS")
            print(self)
            return
            # then apply a 3x2 puzzle move string to move target_tile to i,0
            all_moves += 'ruldrdlurdluurddlur'
            self.update_puzzle('ruldrdlurdluurddlur')
            zero_row, zero_col = self.current_position(0, 0)
            # finally end by moving zero tile to end of row i-1
            all_moves += 'r' * (self._width - 1 - zero_col)
            self.update_puzzle('r' * (self._width - 1 - zero_col))

        print(all_moves)
        # assert self.lower_row_invariant(target_row - 1, self._width - 1)
        return all_moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        # descending order from left to right and zeroth tile at row 0, last col
        # get the target_tile to row + 1, last col - 1
        #
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

# fifteen = Puzzle(4, 4)
# print(fifteen)
