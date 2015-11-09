import unittest
from solitaire_tantrix import Tantrix


class TestSolitaireMantrix(unittest.TestCase):

    SOLITAIRE_CODES = [
        "BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
        "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"
    ]
    DIRECTIONS = {
        0: (-1, 0, 1),
        1: (-1, 1, 0),
        2: (0, 1, -1),
        3: (1, 0, -1),
        4: (1, -1, 0),
        5: (0, -1, 1)
    }

    def test_basic_methods(self):
        # create an instance of class Tantrix
        game_tantrix = Tantrix(6)
        self.assertIs(type(game_tantrix), Tantrix)
        # test tile exists
        print(game_tantrix)
        self.assertEqual(game_tantrix.tile_exists((0, 0, 6)), True)
        # test tiling size
        self.assertEqual(game_tantrix.get_tiling_size(), 6)
        self.assertEqual(game_tantrix.tile_exists((0, 0, 6)), True)
        # test remove tile
        game_tantrix.remove_tile((0, 0, 6))
        self.assertEqual(game_tantrix.tile_exists((0, 0, 6)), False)
        # test place tile
        game_tantrix.place_tile(((0, 0, 6)), 'BBRRYY')
        self.assertEqual(game_tantrix.tile_exists((0, 0, 6)), True)
        # test get neighbor
        computed = game_tantrix.get_neighbor((0, 0, 6), 2)
        self.assertEqual(computed, (0, 1, 5))


if __name__ == '__main__':
    unittest.main(verbosity=2)
