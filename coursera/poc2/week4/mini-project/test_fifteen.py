import unittest
from fifteen import Puzzle


class TestFifteen(unittest.TestCase):
    def test_lower_row_invariant(self):
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0], fifteen._grid[2][1] = fifteen._grid[2][1], \
                                                   fifteen._grid[0][0]
        self.assertEqual(fifteen.lower_row_invariant(2, 1), True)
        # now let's create a situation where the invariant does NOT hold
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0], fifteen._grid[2][1] = fifteen._grid[2][1], \
                                                   fifteen._grid[0][0]
        fifteen._grid[0][1], fifteen._grid[3][2] = fifteen._grid[3][2], \
                                                   fifteen._grid[0][1]
        self.assertEqual(fifteen.lower_row_invariant(2, 1), False)
        # now let's check if the invariant holds in the starting postition
        fifteen = Puzzle(4, 4)
        self.assertEqual(fifteen.lower_row_invariant(0, 0), True)
        # now let's create a situation where the invariant does NOT hold
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][1], fifteen._grid[0][2] = fifteen._grid[0][2], \
                                                   fifteen._grid[0][1]
        print(fifteen)
        self.assertEqual(fifteen.lower_row_invariant(0, 0), False)


if __name__ == '__main__':
    unittest.main()
