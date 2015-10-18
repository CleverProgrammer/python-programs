import zombie_apocalypse_bfs
from unittest import TestCase
from zombie_apocalypse_bfs import Apocalypse

__author__ = 'ChessTastic'


class TestApocalypse(TestCase):
    """
  test cases for the zombie apocalypse class
  """

    def test_clear(self):
        state = Apocalypse(5, 5)
        state.add_human(2, 3)
        state.add_human(1, 2)
        self.assertEqual(state.num_humans(), 2)

        state.clear()
        self.assertEqual(state.num_humans(), 0, "test clear")
        print(state)

    def test_num_zombies(self):
        state = Apocalypse(5, 5)
        state.add_zombie(2, 3)
        self.assertEqual(state.num_zombies(), 1, "test num zombies and add zombies")

    def test_num_humans(self):
        state = Apocalypse(5, 5)
        state.add_human(2, 3)
        self.assertEqual(state.num_humans(), 1, "test num humans and add humans")

    def test_human_and_zombie_generators(self):
        state = Apocalypse(5, 5)
        state.add_human(2, 3)
        state.add_human(0, 3)
        state.add_zombie(1, 3)
        state.add_zombie(3, 3)
        # test human generator
        human_generator = state.humans()
        self.assertEqual(next(human_generator), (2,3), "test human generator")
        self.assertEqual(next(human_generator), (0,3), "test human generator")
        # test zombie generator
        zombie_generator = state.zombies()
        self.assertEqual(next(zombie_generator), (1,3), "test zombie generator")
        self.assertEqual(next(zombie_generator), (3,3), "test zombie generator")

    def test_compute_distance_field(self):
        state = Apocalypse(5, 5)
        state.add_human(2, 3)
        state.add_human(1, 2)
        self.assertEqual(state.num_humans(), 2)
        human_distance_field = state.compute_distance_field(zombie_apocalypse_bfs.HUMAN)
        expected_field = [[3, 2, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 0, 1], [4, 3, 2, 1, 2], [5, 4, 3, 2, 3]]
        self.assertEqual(human_distance_field, expected_field, "test distance_field")
        # all cells have been visited after the distance_field computation. No visited grid cells should be empty.
        self.assertEqual(state.visited.is_empty(1, 2), False, "test visited")
        self.assertEqual(state.visited.is_empty(1, 1), False, "test visited")
        # some print statements for debugging purposes.
        print("human_distance_field:")
        for row in human_distance_field:
            print(row)
        print()
        print("human_list:", state._human_list)
        print("boundary:", state.boundary)
        print("visited grid: \n%s" % state.visited)
