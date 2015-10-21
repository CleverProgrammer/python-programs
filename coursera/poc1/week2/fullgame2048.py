# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:41:42 2015
Clone of 2048 game.
The code skulptor link to the full game:
http://www.codeskulptor.org/#user40_vlzFutJJ5c_32.py
@author: rafeh
"""
# import poc_2048_gui
import unittest
from random import choice
from random import randint

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    slide = [num for num in line if num]
    pairs = []
    for idx, num in enumerate(slide):
<<<<<<< HEAD:coursera/poc1/fullgame2048.py
        if idx == len(slide)-1:
            pairs.append(num)
            break
        elif num == slide[idx+1]:
            pairs.append(num*2)
            slide[idx+1] = None
=======
        if idx == len(slide) - 1:
            pairs.append(num)
            break
        elif num == slide[idx + 1]:
            pairs.append(num * 2)
            slide[idx + 1] = None
>>>>>>> problems:coursera/poc1/week2/fullgame2048.py
        else:
            pairs.append(num)
    slide = [pair for pair in pairs if pair]
    slide.extend([0] * (len(line) - len(slide)))
    return slide


class TwentyFortyEight:

    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initializing the board
        """
        self._rows = grid_height
        self._columns = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
<<<<<<< HEAD:coursera/poc1/fullgame2048.py
        self._board = [[0 for dummy_col in range(self._columns)] \
                        for dummy_row in range(self._rows)]
=======
        self._board = [[0 for dummy_col in range(self._columns)]
                       for dummy_row in range(self._rows)]
>>>>>>> problems:coursera/poc1/week2/fullgame2048.py
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        counter = 0
        string_grid = '['
        for idx in self._board:
            if counter < len(self._board) - 1:
                string_grid += str(idx) + "\n"
                counter += 1
            else:
                string_grid += str(idx) + "]"

        return string_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._rows

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._columns

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == LEFT:
            self._board = [merge(row) for row in self._board]

        elif direction == RIGHT:
            self._board = [merge(row[::-1])[::-1] for row in self._board]

        else:
            for idx in range(self._columns):
                column = [row[idx] for row in self._board]  # 0th column
                if direction == DOWN:
                    merged_column = merge(column[::-1])[::-1]
                else:
                    merged_column = merge(column)
                for row, value in zip(self._board, merged_column):
                    row[idx] = value
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
<<<<<<< HEAD:coursera/poc1/fullgame2048.py
        zeros_indices = [(r, c) for r, row in enumerate(self._board) \
=======
        zeros_indices = [(r, c) for r, row in enumerate(self._board)
>>>>>>> problems:coursera/poc1/week2/fullgame2048.py
                         for c, cell in enumerate(row) if not cell]
        value = 2
        if randint(1, 10) == 10:  # 10% chance of being 4.
            value = 4
        if zeros_indices:
            random_zero_index = choice(zeros_indices)
            self._board[random_zero_index[0]][random_zero_index[1]] = value

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]

# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


class TestFullGame2048(unittest.TestCase):

    def testMerge(self):
        self.assertEqual(merge([0, 0, 2, 2]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 0, 2, 4]), [4, 4, 0, 0])
        self.assertEqual(merge([2, 2, 0, 0]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])
        self.assertEqual(merge([8, 16, 16, 8]), [8, 32, 8, 0])
        self.assertEqual(merge([8, 16, 16, 8, 2, 6]), [8, 32, 8, 2, 6, 0])

    def test__init__(self):
        self.assertIsInstance(TwentyFortyEight(5, 5), TwentyFortyEight)

    def test__str__(self):
        self.assertIsInstance(TwentyFortyEight(5, 5).__str__(), str)
        print("\n\nNew Game" + str(TwentyFortyEight(5, 5)))

    def test_get_grid_height(self):
        self.assertEqual(TwentyFortyEight(3, 5).get_grid_height(), 3)
        self.assertEqual(TwentyFortyEight(20, 5).get_grid_height(), 20)
        self.assertNotEqual(TwentyFortyEight(5, 20).get_grid_height(), 20)

    def test_get_grid_width(self):
        self.assertEqual(TwentyFortyEight(3, 20).get_grid_width(), 20)
        self.assertEqual(TwentyFortyEight(20, 5).get_grid_width(), 5)
        self.assertNotEqual(TwentyFortyEight(5, 20).get_grid_width(), 5)

    def test_new_tile(self):
        probability = [TwentyFortyEight(5, 5).new_tile() for i in range(1000)]
        self.assertLess(probability.count(4), len(probability) * .15)
        a = TwentyFortyEight(5, 5)
        a.new_tile()
        print(" \nnew_tile function" + str(a))
        # self.assertIsInstance(TwentyFortyEight(5, 5).new_tile(), tuple)

    def test_set_tile(self):
        # self.assertIsInstance(TwentyFortyEight(5, 5).set_tile(3, 1, 5), list)
        a = TwentyFortyEight(5, 5)
        a.set_tile(3, 1, 5)
        # self.assertEqual(a.board[3][1], 5)
        print(" \nset_tile function" + str(a))

    def test_get_tile(self):
        a = TwentyFortyEight(5, 5)
        a.set_tile(3, 1, 5)
        self.assertEqual(a.get_tile(3, 1), 5)

    def test_move_left(self):
        obj = TwentyFortyEight(5, 5)
        for _ in range(6):
            obj.new_tile()
        print("\ntest move" + str(obj))
        obj.move(LEFT)
        print("\ntest move" + str(obj))

    def test_move_right(self):
        obj = TwentyFortyEight(5, 5)
        for _ in range(6):
            obj.new_tile()
        print("\ntest move" + str(obj))
        obj.move(RIGHT)
        print("\ntest move" + str(obj))

    def test_move_down(self):
        obj = TwentyFortyEight(5, 5)
        for _ in range(30):
            obj.new_tile()
        print("\ntest move" + str(obj))
        obj.move(DOWN)
        print("\ntest move" + str(obj))

suite = unittest.TestLoader().loadTestsFromTestCase(TestFullGame2048)
unittest.TextTestRunner(verbosity=2).run(suite)
