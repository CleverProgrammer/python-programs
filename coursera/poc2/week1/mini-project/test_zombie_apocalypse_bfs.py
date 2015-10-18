__author__ = 'ChessTastic'


import unittest
from zombie_apocalypse_bfs import Apocalypse

class TestClassApocalypse(unittest.TestCase):

    def test_distances(self):
            state = Apocalypse(2, 3, zombie_list = [(0, 0)])



if __name__ == '__main__':
    unittest.main(exit=False)