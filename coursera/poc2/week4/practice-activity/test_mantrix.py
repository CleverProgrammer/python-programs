from solitaire_tantrix import Tantrix
import unittest

class TestSolitaireMantrix(unittest.TestCase):


    SOLITAIRE_CODES = [
        "BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
        "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"
    ]


    def test_basic_methods(self):
        # create an instance of class Tantrix
        game_tantrix = Tantrix(6)
        self.assertIs(type(game_tantrix), Tantrix)
        # test tile exists
        print(game_tantrix)
        self.assertEqual(game_tantrix.tile_exists((0, 0, 6)), True) 
        # test tiling size
        self.assertEqual(game_tantrix.get_tiling_size(), 6)
        # test remove tile
        game_tantrix.remove_tile((0, 0, 6))
        self.assertEqual(game_tantrix.tile_exists((0, 0, 6)), False) 
        # test place_tile
        game_tantrix.place_tile(((0, 0, 6)), 'BBRRYY')
        self.assertEqual(game_tantrix.tile_exists((0, 0, 6)), True) 


if __name__ == '__main__':
    unittest.main(verbosity=2)
