# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:41:42 2015

@author: rafeh
"""

"""
Clone of 2048 game.
"""
import unittest
#import poc_2048_gui

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
    >>> merge([2, 0, 2, 4])
    [4, 4, 0, 0]
    >>> merge([0, 0, 2, 2])
    [4, 0, 0, 0]
    >>> merge([2, 2, 0, 0])
    [4, 0, 0, 0]
    >>> merge([2, 2, 2, 2, 2])
    [4, 4, 2, 0, 0]
    >>> merge([8, 16, 16, 8])
    [8, 32, 8, 0]
    """
    pairs = []
    prev = None
    for num in line:
        if not num:
            continue
        if prev is None:
            prev = num
        elif num == prev:
            pairs.append(num+prev)
            prev = None
        else:
            pairs.append(prev)
            prev = num
    if prev is not None:  # Append last value if non-zero
        pairs.append(prev)
    pairs.extend([0] * (len(line) - len(pairs)))
    return pairs

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initializing the board
        """
        self.
        self.board = [[row+col for col in range(grid_width)] \
                         for row in range(grid_height)]


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """

        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
class TestFullGame2048(unittest.TestCase):

    def test_merge(self):
        self.assertEqual(merge([0, 0, 2, 2]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 0, 2, 4]), [4, 4, 0, 0])
        self.assertEqual(merge([2, 2, 0, 0]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])
        self.assertEqual(merge([8, 16, 16, 8]), [8, 32, 8, 0])
        self.assertEqual(merge([8, 16, 16, 8, 2, 6]), [8, 32, 8, 2, 6, 0])


suite = unittest.TestLoader().loadTestsFromTestCase(TestFullGame2048)
unittest.TextTestRunner(verbosity=2).run(suite)
