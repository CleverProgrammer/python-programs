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
        """
        returns a solved board configuration to check against
        """
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

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        target_current_row, target_current_col = self.current_position(target_row, target_col)
        all_moves = ""
        if target_current_row < target_row:
            all_moves += 'u' * (target_row - target_current_row)
            self.update_puzzle('u' * (target_row - target_current_row))
            if target_current_col < target_col:
                all_moves += 'l' * (target_col - target_current_col)
                self.update_puzzle('l' * (target_col - target_current_col))
                _, target_current_col = self.current_position(target_row, target_col)
                all_moves += 'drrul' * (target_col - target_current_col)
                self.update_puzzle('drrul' * (target_col - target_current_col))
                all_moves += 'drul'
                self.update_puzzle('drul')
                target_current_row, _ = self.current_position(target_row, target_col)
                all_moves += 'ddrul' * (target_row - target_current_row)
                self.update_puzzle('ddrul' * (target_row - target_current_row))
                all_moves += 'd'
                self.update_puzzle('d')

            elif target_current_col == target_col:
                all_moves += 'l'
                self.update_puzzle('l')
                target_current_row, _ = self.current_position(target_row, target_col)
                all_moves += 'ddrul' * (target_row - target_current_row) + 'd'
                self.update_puzzle('ddrul' * (target_row - target_current_row) + 'd')

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
                self.update_puzzle('l')
            elif target_col - target_current_col > 1:
                _, target_current_col = self.current_position(target_row, target_col)
                all_moves += 'l' * (target_col - target_current_col)
                self.update_puzzle('l' * (target_col - target_current_col))
                _, target_current_col = self.current_position(target_row, target_col)
                all_moves += 'urrdl' * (target_col - target_current_col)
                self.update_puzzle('urrdl' * (target_col - target_current_col))
        return all_moves

    def stuff_move(self, target_row, target_col, row, column):
        """
        place a tile at target position;
        target tile's current position must be either above the target position
        (k < i) or on the same row to the left (i = k and l < j);
        returns a move string
        """
        move_things = ''
        combo = 'druld'

        column_movement = target_col - column
        row_movement = target_row - row

        move_things += row_movement * 'u'
        if column_movement == 0:
            move_things += 'ld' + (row_movement - 1) * combo
        else:
            if column_movement > 0:
                move_things += column_movement * 'l'
                if row == 0:
                    move_things += (abs(column_movement) - 1) * 'drrul'
                else:
                    move_things += (abs(column_movement) - 1) * 'urrdl'
            # tile is on the right from target, specific move first
            elif column_movement < 0:
                move_things += (abs(column_movement) - 1) * 'r'
                if row == 0:
                    move_things += abs(column_movement) * 'rdllu'
                else:
                    move_things += abs(column_movement) * 'rulld'
            # apply common move as last
            move_things += row_movement * combo

        return move_things

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0)
        make_the_move = 'ur'
        self.update_puzzle(make_the_move)

        row, column = self.current_position(target_row, 0)
        if row == target_row and column == 0:
            step = (self.get_width() - 2) * 'r'
            self.update_puzzle(step)
            make_the_move += step
        else:
            step = self.stuff_move(target_row - 1, 1, row, column)
            step += 'ruldrdlurdluurddlu' + (self.get_width() - 1) * 'r'
            self.update_puzzle(step)
            make_the_move += step

        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1)
        return make_the_move

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        check whether the puzzle satisfies the row zero invariant at the given column (col > 1);
        returns a boolean
        """
        if not self.get_number(0, target_col) == 0:
            return False

        for column in range(self.get_width()):
            for row in range(self.get_height()):
                if (row == 0 and column > target_col) or (row == 1 and column >= target_col) or row > 1:
                    if not (row, column) == self.current_position(row, column):
                        return False

        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        zero_row, zero_col = self.current_position(0, 0)
        if (zero_row, zero_col) == (1, target_col):
            if self.lower_row_invariant(1, target_col):
                return True
        return False

    def solve_row0_tile(self, target_col):
        """
        solve the tile in row zero at the specified column;
        updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col)
        move_it = 'ld'
        self.update_puzzle(move_it)

        row, column = self.current_position(0, target_col)
        if row == 0 and column == target_col:
            return move_it
        else:
            step = self.stuff_move(1, target_col - 1, row, column)
            step += 'urdlurrdluldrruld'
            self.update_puzzle(step)
            move_it += step

        return move_it

    def solve_row1_tile(self, target_col):
        """
        solve the tile in row one at the specified column;
        updates puzzle and returns a move string
        """
        row, column = self.current_position(1, target_col)
        move_stuff_around = self.stuff_move(1, target_col, row, column)
        move_stuff_around += 'ur'

        self.update_puzzle(move_stuff_around)
        return move_stuff_around

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        solves the upper left 2x2 part of the puzzle;
        doesn't check for insolvable configuration!,
        updates the puzzle and returns a move string
        """
        move_stuff_around = ''
        beginning_steps = ''

        if self.get_number(1, 1) == 0:
            beginning_steps += 'ul'
            self.update_puzzle(beginning_steps)
            if (0, 1) == self.current_position(0, 1) and (1, 1) == self.current_position(1, 1):
                return beginning_steps

            if self.get_number(0, 1) < self.get_number(1, 0):
                move_stuff_around += 'rdlu'
            else:
                move_stuff_around += 'drul'
            self.update_puzzle(move_stuff_around)

        return beginning_steps + move_stuff_around

    def solve_puzzle(self):
        """
        generate a solution string for a puzzle;
        updates the puzzle and returns a move string
        """
        move_stuff_around = ''

        row = self.get_height() - 1
        column = self.get_width() - 1
        row_current, column_current = self.current_position(0, 0)
        column_delta = column_current - column
        row_delta = row_current - row
        step = abs(column_delta) * 'r' + abs(row_delta) * 'd'
        self.update_puzzle(step)
        move_stuff_around += step

        for dummy_row in range(row, 1, -1):
            for dummy_column in range(column, 0, -1):
                move_stuff_around += self.solve_interior_tile(dummy_row, dummy_column)
            move_stuff_around += self.solve_col0_tile(dummy_row)

        for dummy_column in range(column, 1, -1):
            move_stuff_around += self.solve_row1_tile(dummy_column)
            move_stuff_around += self.solve_row0_tile(dummy_column)

        move_stuff_around += self.solve_2x2()
        return move_stuff_around

# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

# fifteen = Puzzle(4, 4)
# print(fifteen)
