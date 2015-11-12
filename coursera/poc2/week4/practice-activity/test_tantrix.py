import unittest
import solitaire_tantrix
from solitaire_tantrix import Tantrix


class TestSolitaireTantrix(unittest.TestCase):

    SOLITAIRE_CODES = [
        "BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
        "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]
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

    def test_legal_configurations(self):
        solitaire_tantrix.MINIMAL_GRID_SIZE = 1
        game_tantrix = Tantrix(1)
        self.assertEqual(game_tantrix.is_legal(), True)
        # test get all neighbors
        self.assertEqual(game_tantrix.get_all_neighbors((0, 0, 6)), [])
        solitaire_tantrix.MINIMAL_GRID_SIZE = 2
        game_tantrix = Tantrix(2)
        game_tantrix.place_tile((0, 0, 6), 'YYBBRR')
        game_tantrix.place_tile((0, 1, 5), 'RYYRBB')
        game_tantrix.place_tile((1, 0, 5), 'BBYRRY')
        positions_to_remove = []
        for pos in game_tantrix._tile_value:
            if pos not in ((0, 0, 6), (0, 1, 5), (1, 0, 5)):
                positions_to_remove.append(pos)
        for pos in positions_to_remove:
            game_tantrix.remove_tile(pos)
        self.assertEqual(game_tantrix.is_legal(), True)
        game_tantrix.rotate_tile((0, 0, 6))
        self.assertEqual(game_tantrix.is_legal(), False)

    def test_loop(self):
        solitaire_tantrix.MINIMAL_GRID_SIZE = 2
        game_tantrix = Tantrix(2)
        game_tantrix.place_tile((0, 0, 6), 'RRYYBB')
        game_tantrix.place_tile((0, 1, 5), 'YRBBRY')
        game_tantrix.place_tile((1, 0, 5), 'YRRYBB')
        positions_to_remove = []
        for pos in game_tantrix._tile_value:
            if pos not in ((0, 0, 6), (0, 1, 5), (1, 0, 5)):
                positions_to_remove.append(pos)
        for pos in positions_to_remove:
            game_tantrix.remove_tile(pos)
        self.assertEqual(game_tantrix.has_loop('B'), True)
        # test get all neighbors
        expected = [(0, 1, 5), (1, 0, 5)]
        self.assertEqual(game_tantrix.get_all_neighbors((0, 0, 6)), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
