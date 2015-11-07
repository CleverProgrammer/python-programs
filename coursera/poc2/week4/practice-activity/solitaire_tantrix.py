"""
solitaire tantrix: A game containing a grid of colored hexagonal tiles.
1. Model a hexagonal grid
2. Implement basic Tantrix methods
3. Detect whether a position is legal
4. Check for a win
- 4 sets of 14 tiles
- total of 56 total tiles
- Only four colors, red/blue/green/yellow or RBGY
- 6 letter string can describe the pattern of any tile going clockwise

======== COURSERA NOTES ===========
Student facing code for Tantrix Solitaire
http://www.jaapsch.net/puzzles/tantrix.htm

Game is played on a grid of hexagonal tiles.
All ten tiles for Tantrix Solitaire and place in a corner of the grid.
Click on a tile to rotate it.  Cick and drag to move a tile.

Goal is to position the 10 provided tiles to form
a yellow, red or  blue loop of length 10
======== END COURSERA NOTES =========
"""


# Core modeling idea - a triangular grid of hexagonal tiles are
# model by integer tuples of the form (i, j, k)
# where i + j + k == size and i, j, k >= 0.

# Each hexagon has a neighbor in one of six directions
# These directions are modeled by the differences between the
# tuples of these adjacent tiles

# Numbered directions for hexagonal grid, ordered clockwise at 60 degree
# intervals
# directed are given as a tuple of 3 coordinates
DIRECTIONS = {
     0 : (-1, 0, 1),
     1  : (-1, 1, 0),
     2 : (0, 1,-1),
     3 : (1, 0,-1),
     4 : (1,-1, 0),
     5 : (0,-1, 1)
}


def reverse_direction(direction):
    """
    Helper function that returns opposite direction on hexagonal grid
    """
    num_directions = len(DIRECTIONS)
    return (direction + num_directions / 2) % num_directions


# Color codes for ten tiles in Tantrix Solitaire
# "B" denotes "Blue", "R" denotes "Red", "Y" denotes "Yellow"
SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                   "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]


# Minimal size of grid to allow placement of 10 tiles
MINIMAL_GRID_SIZE = 4  # effects how many pieces there are on the board


class Tantrix:
    """
    Basic Tantrix game class
    """

    def __init__(self, size):
        """
        Create a triangular grid of hexagons with size + 1 tiles on each side.
        """
        assert size >= MINIMAL_GRID_SIZE
        self._tiling_size = size  # the overall board size. (6 by default)

        # Initialize dictionary tile_value to contain codes for ten
        # tiles in Solitaire Tantrix in one 4x4 corner of grid
        self._tile_value = {}  # models the hexagonal grid
        #outerloop or i should run the same amount of times as the MINIMAL_GRID_SIZE
        for index_i in range(MINIMAL_GRID_SIZE):
            for index_j in range(MINIMAL_GRID_SIZE
        # the size of the inner loop or j should reduce by 1 every time
        # k should always be decreasing

    def __str__(self):
        """
        Return string of dictionary of tile positions and values
        """
        return str(self._tile_value)

    def get_tiling_size(self):
        """
        Return size of board for GUI
        """
        return self._tiling_size


    def tile_exists(self, index):

        """
        Return whether a tile with given index exists
        """
        if self._tiling_size[index]:
            return True
        return False

    def place_tile(self, index, code):
        """
        Play a tile with code at cell with given index
        : param index : tuple
        : param code  : string
        """
        self._tiling_size[index] = code  # index or key in dictionary

    def remove_tile(self, index):
        """
        Remove a tile at cell with given index and return the code value for that tile   
        : param : tuple (dictionary key)
        """
        self._tile_value.pop(index)

    def rotate_tile(self, index):
        """
        Rotate a tile clockwise at cell with given index
        original code ==> 'BBRRYY'
        > rotate_tile((0, 0, 6))
        new code      ==> 'YBBRRY'
        """
        original = self._tile_value[index]
        new  = original[-1] + original[:-1]
        self._tile_value[index] = new

    def get_code(self, index):
        """
        Return the code of the tile at cell with given index
        : param  : position tuple (dictionary key)
        : return : string (6 letter code)
        """
        return self._tile_value[index]  # access the dictionary value

    def get_neighbor(self, index, direction):
        """
        Return the index of the tile neighboring the tile with given index in
        given direction
        """
        return ()

    def is_legal(self):
        """
        Check whether a tile configuration obeys color matching rules for
        adjacent tiles
        """
        return False

    def has_loop(self, color):
        """
        Check whether a tile configuration has a loop of size 10 of given color
        """
        return False

    def position_checker(self, hexgrid):
        """
        Take in any code from the list SOLITAITE_CODES and check it against
        self._tile_value that models the hexagonal grid
        key should be (0, 0, 6)
        value should be "BBRRYY"
        : param  : dictionary value
        : return : tuple (dictionary key)
        SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                   "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]
        >>> position_checker("BBRRYY")
        (0, 0, 6)
        >>> position_checker("BBRYYR")
        (0, 1, 5)
        >>> position_checker("BBYRRY")
        (0, 2, 4)
        >>> position_checker("BRYBYR")
        (1, 0, 5)
        >>> position_checker("RBYRYB")
        (1, 1, 4)
        >>> position_checker("YBRYRB")
        (1, 2, 3)
        """
        pass


# run GUI for Tantrix
# import poc_tantrix_gui
# poc_tantrix_gui.TantrixGUI(Tantrix(6))
if __name__ == '__main__':
    import doctest
    doctest.testmod()
