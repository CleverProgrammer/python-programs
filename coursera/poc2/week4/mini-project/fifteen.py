"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""


# import poc_fifteen_gui

# noinspection PyMethodMayBeStatic,PyUnreachableCode,PyProtectedMember
class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None, id_=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self.id = id_
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
        if self.id is not None:
            puzzle_info = str(self.id) + '\n' + ans
        else:
            puzzle_info = ans
        return puzzle_info

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

    def current_location(self, number):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                if self._grid[row][col] == number:
                    return row, col

    def helper_solve_interior(self, target_solved_row, target_solved_col, zero_row, zero_col,
                              solved_val_row, solved_val_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        :param target_solved_row: give me the solved row of the number you want moved
        :param target_solved_col: give me the solved col of the number you want moved
        :param zero_row:  give me the row of zero
        :param zero_col:  give me the col of zero
        :return: string
        """
        target_current_row, target_current_col = self.current_position(target_solved_row,
                                                                       target_solved_col)
        want_moved = self.get_number(target_current_row, target_current_col)
        replace_with = self.get_number(solved_val_row, solved_val_col)
        self.set_number(target_current_row, target_current_col, replace_with)
        self.set_number(solved_val_row, solved_val_col, want_moved)
        print('SWAPPED VALUES', self)
        all_moves = self.solve_interior_tile(zero_row, zero_col)
        # AMAZING Rosuav trick!!!!
        wm = self.current_location(want_moved)
        self.set_number(*self.current_location(replace_with), value=want_moved)
        self.set_number(*wm, value=replace_with)
        print('LEAVING HELPER_SOLVE_INTERIOR')
        print(self)
        return all_moves

    def solve_interior_tile(self, target_row, target_col):
        """

        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        print("ENTERING SOLVE_INTERIOR_TILE")
        print(self)
        # print()
        target_current_row, target_current_col = self.current_position(target_row, target_col)
        # HERE
        # print('solving for:',
        # self.get_number(target_current_row, target_current_col))
        all_moves = ""
        # if the target tile is above me
        # step 1: get to the row
        # step 2: do the cyclic motion and bring it my position
        # step 3: place myself at (target_row, target_col - 1)
        if target_current_row < target_row:
            all_moves += 'u' * (target_row - target_current_row)
            self.update_puzzle('u' * (target_row - target_current_row))

            # if the target tile is above me and to the left
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

            # if the target tile is above me and to the right
            # ******* SOMETHING IS WRONG WITH THIS LOGIC *******
            elif target_current_col > target_col:
                # print(self)
                # print('it is above me and to the right')
                all_moves += 'r' * (target_current_col - target_col)
                self.update_puzzle('r' * (target_current_col - target_col))
                zero_row, zero_col = self.current_location(0)
                if zero_row > 0:
                    _, target_current_col = self.current_position(target_row, target_col)
                    # print(target_current_col, target_col)
                    if target_current_col == target_col:
                        all_moves += 'ull'
                        self.update_puzzle('ull')
                        # print('CUZ\n', self)
                        target_current_row, _ = self.current_position(target_row, target_col)
                        all_moves += 'ddrul' * (target_row - target_current_row)
                        self.update_puzzle('ddrul' * (target_row - target_current_row))
                        all_moves += 'd'
                        self.update_puzzle('d')
                else:
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
                # _, target_current_col = self.current_position(target_row, target_col)
                # ll urrdl
                # left * (target_col - target_current_col)
                all_moves += 'l' * (target_col - target_current_col)
                self.update_puzzle('l' * (target_col - target_current_col))
                _, target_current_col = self.current_position(target_row, target_col)
                all_moves += 'urrdl' * (target_col - target_current_col)
                self.update_puzzle('urrdl' * (target_col - target_current_col))
            elif target_current_col - target_col >= 1:
                print('SO THATS THE PROBLEM')
                all_moves += 'r' * (target_current_col - target_col)
                self.update_puzzle('r' * (target_current_col - target_col))
                # print('elif of sit\n', self)
                _, target_current_col = self.current_position(target_row, target_col)
                # print('tcc - tc:', target_current_col - target_col)
                all_moves += 'ulldr' * (target_current_col - target_col)
                self.update_puzzle('ulldr' * (target_current_col - target_col))
                all_moves += 'ulld'
                self.update_puzzle('ulld')
        # problem is that it doesn't do anything if it's on the same row and on right side
        print('LEAVING SOLVE_INTERIOR_TILE')
        print(self)
        return all_moves

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # get position of 15 as target_solved_row, target_solved_col

        assert target_row > 1
        assert self.lower_row_invariant(target_row, 0)
        # give me the solved row and col of what I want
        # print('HA:', target_solved_row, target_solved_col)
        all_moves = 'ur'
        self.update_puzzle('ur')
        # LUCKY CASE when just 'ur' solves the problem
        if self.current_position(target_row, 0) == (target_row, 0):
            # get current position of zero tile
            zero_row, zero_col = self.current_position(0, 0)
            # move all the way to the right
            all_moves += 'r' * (self._width - 1 - zero_col)
            self.update_puzzle('r' * (self._width - 1 - zero_col))
        elif self.current_position(target_row, 0) != (target_row, 0):
            # print('suP:', target_row)
            zero_row, zero_col = self.current_position(0, 0)
            # print('zero stuff:', zero_row, zero_col)
            # print('suPTwOoo:\n', self)
            solved_val_row, solved_val_col = self.current_position(zero_row, zero_col)
            # print('svr and svc:', solved_val_row, solved_val_col)
            # helper_solve_interior updates the position by itself.
            all_moves += self.helper_solve_interior(target_row, 0,
                                                    zero_row, zero_col,
                                                    solved_val_row, solved_val_col)
            print('==after solve_interior call inside of solve_col0==\n', self)
            all_moves += 'ruldrdlurdluurddlur'
            self.update_puzzle('ruldrdlurdluurddlur')
            zero_row, zero_col = self.current_position(0, 0)
            all_moves += 'r' * (self._width - 1 - zero_col)
            self.update_puzzle('r' * (self._width - 1 - zero_col))

        # assert self.lower_row_invariant(target_row - 1, self._width - 1)
        return all_moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        check whether the puzzle satisfies the row zero invariant at the given column (col > 1);
        returns a boolean
        """
        board = self.clone()
        solved_board = self.solved_board()
        if solved_board[0][target_col + 1:] == self._grid[0][target_col + 1:]:
            if solved_board[1][target_col] == self._grid[1][target_col]:
                board.set_number(0, target_col, -1)
                board.set_number(1, target_col, 0)
                if board.lower_row_invariant(1, target_col):
                    return True
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self.lower_row_invariant(1, target_col):
            return True
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col)
        solved_board = self.solved_board()
        print('entered solve_row0_tile:\n', self)
        all_moves = 'ld'
        self.update_puzzle('ld')
        if solved_board[0][target_col] == self._grid[0][target_col]:
            return all_moves
        zero_row, zero_col = self.current_position(0, 0)
        solved_val_row, solved_val_col = (self.current_position(zero_row, zero_col))
        all_moves += self.helper_solve_interior(target_solved_row=0,
                                                target_solved_col=target_col,
                                                zero_row=zero_row, zero_col=zero_col,
                                                solved_val_row=solved_val_row,
                                                solved_val_col=solved_val_col)
        all_moves += 'urdlurrdluldrruld'
        self.update_puzzle('urdlurrdluldrruld')
        return all_moves

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        print('ENTERED solve_row1_tile')
        print('target_col:', target_col)
        print(self)
        assert self.row1_invariant(target_col)
        all_moves = self.solve_interior_tile(target_row=1, target_col=target_col)
        all_moves += 'ur'
        self.update_puzzle('ur')
        assert self.row0_invariant(target_col)
        print('LEAVING solve_row1_tile')
        print(self)
        return all_moves

    ###########################################################
    # Phase 3 methods

    def legal_moves(self):
        available_moves = ''
        zero_row, zero_col = self.current_position(0, 0)
        if (zero_row, zero_col) == (0, 0):
            available_moves = 'dr'
        elif (zero_row, zero_col) == (0, 1):
            available_moves = 'ld'
        elif (zero_row, zero_col) == (1, 0):
            available_moves = 'ur'
        elif (zero_row, zero_col) == (1, 1):
            available_moves = 'lu'
        return available_moves

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        print('ENTERED SOLVE_2x2')
        print(self)
        import random
        assert self.row1_invariant(1)
        all_moves = ''
        solved_board = self.solved_board()
        known_position = [[solved_board[0][0], solved_board[1][1]],
                          [solved_board[0][1], solved_board[1][0]]
                          ]
        print(self._grid[0][:2])
        print(self._grid[1][:2])
        print(known_position[0][:2])
        print(known_position[1][:2])
        # [ [0, 5], [1, 4] ]
        print(self._grid)
        # shuffle till you get to a known position
        # no possible way to reach certain positions
        clockwise_mapping = {(0, 0): 'rdlu',
                             (0, 1): 'dlur',
                             (1, 0): 'urdl',
                             (1, 1): 'lurd'}
        zero_row, zero_col = self.current_position(0, 0)
        clockwise_moves = clockwise_mapping[(zero_row, zero_col)] * 5
        for clockwise_move in clockwise_moves:
            all_moves += clockwise_move
            self.update_puzzle(clockwise_move)
            if self._grid[0][:2] == solved_board[0][:2] and \
                            self._grid[1][:2] == solved_board[1][:2]:
                return all_moves
                # return all moves
                # self.update_puzzle(clockwise_mapping[(zero_row, zero_col)] * 5)

                # while self._grid[0][:2] != known_position[0][:2] or \
                #                 self._grid[1][:2] != known_position[1][:2]:
                #     legal_moves = self.legal_moves()
                #     # print(legal_moves)
                #     pick_legal_move = random.choice(legal_moves)
                #     # print(pick_legal_move)
                #     all_moves += pick_legal_move
                #     self.update_puzzle(pick_legal_move)
                # move clockwise
                # print('HELLO:', self)
                # now solve the known position
                # if self._grid[0][:2] == known_position[0][:2] and \
                #                 self._grid[1][:2] == known_position[1][:2]:
                #     all_moves += 'rdlurdlu'
                #     self.update_puzzle('rdlurdlu')
        print('LEAVING SOLVE_2x2')
        print(self)
        return 'NOT SOLVABLE'

    def move(self, target_row, target_col):
        """
        takes in a target location to go to and then moves the zero tile there legally.
        updates the puzzle and returns the move string
        :return: move string
        """
        # get the current location of 0
        all_moves = ''
        zero_row, zero_col = self.current_location(0)
        if target_row > zero_row:
            all_moves += 'd' * (target_row - zero_row)
            self.update_puzzle('d' * (target_row - zero_row))
        if target_row < zero_row:
            all_moves += 'u' * (zero_row - target_row)
            self.update_puzzle('u' * (zero_row - target_row))
        if target_col > zero_col:
            all_moves += 'r' * (target_col - zero_col)
            self.update_puzzle('r' * (target_col - zero_col))
        if target_col < zero_col:
            all_moves += 'l' * (zero_col - target_col)
            self.update_puzzle('l' * (zero_col - target_col))
        return all_moves

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        all_moves = ''
        solved_board = self.solved_board()
        board_copy = self.clone()
        reversed_grid = []
        # if it is already solved
        if solved_board != self._grid:
            for row in board_copy._grid[::-1]:
                reversed_grid.append(row[::-1])
        else:
            return ''
        # if it's NOT already solved
        print(reversed_grid)
        row, col = self.current_location(reversed_grid[0][0])
        all_moves = self.move(row, col)
        interior_counter = 0
        col0_counter = 0
        row1_counter = 0
        row0_counter = 0
        solve_2x2_counter = 0
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                # target_row, target_col = self.current_location(reversed_grid[row][col])
                target_row, target_col = self.current_location(0)
                # last bottom right square
                if (target_row, target_col) == (self.get_height() - 1, self.get_width() - 1):
                    if self.get_height() > 2 and self.get_width() > 2:
                        interior_counter += 1
                        print('================IN FIRST IF=================')
                        all_moves += self.solve_interior_tile(target_row, target_col)
                        print('after first if\n', self)
                if target_row == 1 and target_col == 1:
                    print('===============calling solve_2x2=============')
                    all_moves += self.solve_2x2()
                    print(self)
                    solve_2x2_counter += 1
                    return all_moves
                elif target_row == 0:
                    print('===============calling solve_row0_tile=============')
                    all_moves += self.solve_row0_tile(target_col)
                    print(self)
                    row0_counter += 1
                elif target_row == 1:
                    print('===============calling solve_row1_tile=============')
                    all_moves += self.solve_row1_tile(target_col)
                    print(self)
                    row1_counter += 1
                elif target_row > 1 and target_col == 0:
                    print('===============calling solve_col0_tile=============')
                    # print(target_row)
                    # print('YOOOOO')
                    all_moves += self.solve_col0_tile(target_row)
                    print(self)
                    col0_counter += 1
                elif self.lower_row_invariant(target_row, target_col) and \
                        not self.row1_invariant(target_col):
                    interior_counter += 1
                    print('================{0}. IN ELIF================='.format(interior_counter - 1))
                    print('target_row, target_col', (target_row, target_col))
                    print(self)
                    all_moves += self.solve_interior_tile(target_row, target_col)
                    print('after second elif\n', self)
                    # now that all bottom row methods are completed, time to work on the top 2 rows
                    # if interior_counter + col0_counter + row1_counter + row0_counter \
                    #         + solve_2x2_counter == 12:
                    #     print('solve_interior_tile was called {0} times'.format(interior_counter))
                    #     print('solve_col0_tile was called {0} times'.format(col0_counter))
                    #     print('solve_row0_tile was called {0} times'.format(row0_counter))
                    #     print('solve_row1_tile was called {0} times'.format(row1_counter))
                    #     print('solve_2x2 was called {0} times'.format(solve_2x2_counter))
                    #     print('FINAL position')
                    #     return

                    # if row > 1 and col > 0:
                    #     if not self.lower_row_invariant(row, col):
                    #         # move the zero to the first unsolved number on bottom right
                    #         self.move(row, col)
                    #         self.solve_interior_tile(row, col)
                    #         counter += 1
                    #         if counter == 2:
        print('=============DID NOT GET CAUGHT IN ANY IF STATEMENTS==============')
        print('solve_interior_tile was called {0} times'.format(interior_counter))
        print('solve_col0_tile was called {0} times'.format(col0_counter))
        print('FINAL position')
        return all_moves

# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

# fifteen = Puzzle(4, 4)
# print(fifteen)
