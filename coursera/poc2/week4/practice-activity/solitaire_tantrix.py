"""
solitaire tantrix: A game containing a grid of colored hexagonal tiles.
Link: http://www.codeskulptor.org/#user40_1k0MMWM8rp_0.py
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
     0: (-1, 0, 1),  # bottom right neighbor [0][3]  +3
     1: (-1, 1, 0),  # bottom neighbor       [1][-2] +3  find rfind
     2: (0, 1, -1),  # bottom left neighbor  [3][0]  +3  find rfind
     3: (1, 0, -1),  # top left neighbor     [2][5]  -3  rfind find
     4: (1, -1, 0),  # top neighbor          [-2][1] -3
     5: (0, -1, 1),  # top right neighbor    [5][2]  -3
}


def reverse_direction(direction):
    """
    Helper function that returns opposite direction on hexagonal grid
    """
    num_directions = len(DIRECTIONS)
    return (direction + num_directions // 2) % num_directions


# Color codes for ten tiles in Tantrix Solitaire
# "B" denotes "Blue", "R" denotes "Red", "Y" denotes "Yellow"
SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                   "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]


# Minimal size of grid to allow placement of 10 tiles
MINIMAL_GRID_SIZE = 2  # effects how many pieces there are on the board


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
        # outerloop or i should run the same amount of times as the
        # MINIMAL_GRID_SIZE
        self._tile_value = {}  # models the hexagonal grid
        code_idx = 0
        for idx_i in range(MINIMAL_GRID_SIZE):
            # after every outer loop iteration, i and j switch powers
            # meaning that i increases and j decreases
            for idx_j in range(MINIMAL_GRID_SIZE - idx_i):
                # now we just take out i and j out of size to get k
                idx_k = self._tiling_size - (idx_i + idx_j)
                grid_index = (idx_i, idx_j, idx_k)
                self.place_tile(grid_index, SOLITAIRE_CODES[code_idx])
                code_idx += 1
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
        : param  : tuple (dictionary key)
        : return : boolean
        """
        return index in self._tile_value

    def place_tile(self, index, code):
        """
        Play a tile with code at cell with given index
        : param index : tuple
        : param code  : string
        """
        self._tile_value[index] = code  # index or key in dictionary

    def remove_tile(self, index):
        """
        Remove a tile at cell with given index and return the code value for
        that tile
        : param : tuple (dictionary key)
        """
        return self._tile_value.pop(index)

    def rotate_tile(self, index):
        """
        Rotate a tile clockwise at cell with given index
        original code ==> 'BBRRYY'
        > rotate_tile((0, 0, 6))
        new code      ==> 'YBBRRY'
        """
        original = self._tile_value[index]
        new = original[-1] + original[:-1]
        self._tile_value[index] = new

    def get_code(self, index):
        """
        Return the code of the tile at cell with given index
        : param index : position tuple (dictionary key)
        : return      : string (6 letter code)
        """
        return self._tile_value[index]  # access the dictionary value

    def get_neighbor(self, index, direction):
        """
        Return the index of the tile neighboring the tile with given index in
        given direction
        : param index     : tuple (dictonary key of a tile)
        : param direction : number (dictionary key from DIRECTIONS dict)
        : return          : tuple (add the params and return as index of neighb)
        """
        return tuple(map(sum, zip(index, DIRECTIONS[direction])))

    def get_all_neighbors(self, index):
        all_neighbors = []
        for direction in DIRECTIONS:
            if self.tile_exists(self.get_neighbor(index, direction)):
                all_neighbors.append(self.get_neighbor(index, direction))
        return all_neighbors

    def edges_match(self, index, color, neighbor_index):
        pass

    def is_legal(self):
        """
        Check whether a tile configuration obeys color matching rules for
        adjacent tiles
        """
        for tile_index in self._tile_value:
            tile_code = self._tile_value[tile_index]
            for direction in DIRECTIONS:
                if self.tile_exists(self.get_neighbor(tile_index, direction)):
                    neighbor_index = self.get_neighbor(tile_index, direction)
                    neighbor_code = self._tile_value[neighbor_index]
                    print(reverse_direction(direction))
                    if tile_code[direction] == neighbor_code[
                            reverse_direction(direction)]:
                        continue
                    return False
        # if it passes all the illegal cases, return legal or True.
        return True

    def has_loop(self, color):
        """
        Check whether a tile configuration has a loop of size 10 of given color
        """
        if not self.is_legal():  # check one time if position is illegal
            return False

        # start clean, focus.
        tile_indices = list(self._tile_value.keys())
        start_index = tile_indices[0]
        start_code = self._tile_value[start_index]
        next_direction = start_code.find(color)
        next_index = self.get_neighbor(start_index, next_direction)
        current_length = 1

        # loop through
        # next_index is neighbor
        while start_index != next_index:
            # current index is next neighbor's index
            current_index = next_index
            # if the next neighbor does not exist, return False
            if not self.tile_exists(current_index):
                return False
            # get the current neighbor's code
            current_code = self._tile_value[current_index]
            # if the first color occurrence of neighbor matches with starting
            if current_code.find(color) == reverse_direction(next_direction):
                # 2 == 4
                next_direction = current_code.rfind(color)
            else:
                next_direction = current_code.find(color)
            next_index = self.get_neighbor(current_index, next_direction)
            current_length += 1

        print(len(SOLITAIRE_CODES[:3]))
        return current_length == len(SOLITAIRE_CODES)
