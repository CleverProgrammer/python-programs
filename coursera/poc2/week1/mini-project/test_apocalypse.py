import zombie_apocalypse_bfs
from unittest import TestCase
from zombie_apocalypse_bfs import Apocalypse

__author__ = 'ChessTastic'


class TestApocalypse(TestCase):
    """
  test cases for the zombie apocalypse class
  """

    def test_init(self):
        state = Apocalypse(5, 5,
                           obstacle_list = [(1, 2), (3,4)],
                           zombie_list = [(2,2)],
                           human_list = [(0,4), (4,3)]
                           )
        self.assertEqual(len(state._obstacle_list), 2, "test obstacles list length")
        self.assertEqual(len(state._zombie_list), 1, "test zombies list length")
        self.assertEqual(len(state._human_list), 2, "test humans list length")

    def test_clear(self):
        state = Apocalypse(5, 5)
        state.add_human(2, 3)
        state.add_human(1, 2)
        self.assertEqual(state.num_humans(), 2)
        # test the clear method
        state.clear()
        self.assertEqual(state.num_humans(), 0, "test clear")

    def test_num_zombies(self):
        state = Apocalypse(5, 5)
        state.add_zombie(2, 3)
        self.assertEqual(state.num_zombies(), 1, "test num zombies and add zombies")

    def test_num_humans(self):
        state = Apocalypse(5, 5)
        state.add_human(2, 3)
        self.assertEqual(state.num_humans(), 1, "test num humans and add humans")

    def test_human_and_zombie_and_obstacle_generators(self):
        state = Apocalypse(5, 5, obstacle_list = [(1,2), (3,4), (1,3)])
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
        # test obstacle generator
        obstacle_generator = state.obstacle()
        self.assertEqual(next(obstacle_generator), (1,2), "test obstacle generator")
        self.assertEqual(next(obstacle_generator), (3,4), "test obstacle generator")
        self.assertEqual(next(obstacle_generator), (1,3), "test obstacle generator")

    def test_compute_distance_field(self):
        state = Apocalypse(5, 5)
        state.add_human(2, 3)
        state.add_human(1, 2)
        self.assertEqual(state.num_humans(), 2)
        human_distance_field = state.compute_distance_field(zombie_apocalypse_bfs.HUMAN)
        expected_field = [[3, 2, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 0, 1], [4, 3, 2, 1, 2], [5, 4, 3, 2, 3]]
        self.assertEqual(human_distance_field, expected_field, "test distance_field")
        # some print statements for debugging purposes.
        print("human_distance_field:")
        for row in human_distance_field:
            print(row)
        print()
        print("human_list:", state._human_list)

    def test_move_humans(self):
        state = Apocalypse(5, 5, zombie_list = [(1,2), (2,3)], human_list = [(2,2), (4,4)])
        zombie_distance_field = state.compute_distance_field(zombie_apocalypse_bfs.ZOMBIE)
        print()
        print("-------------------------------")
        print("Zombie Distance Field:")
        for row in zombie_distance_field:
            print(row)
        print()
        human_generator = state.humans()
        human = next(human_generator)
        self.assertEqual(human, (2,2), "test human generator")
        neighbors = state.four_neighbors(human[0], human[1])
        self.assertEqual(neighbors, [(1, 2), (3, 2), (2, 1), (2, 3)], "testing human's neighbors")
        human_distance = zombie_distance_field[human[0]][human[1]]
        print(neighbors[0][0])
        print(zombie_distance_field[neighbors[0][0]][neighbors[0][1]])
        print(human_distance)
        safest_distance = 10
        safest_location = 0
        for neighbor in neighbors:
            print(neighbor)
            print(zombie_distance_field[neighbor[0]][neighbor[1]])
            if zombie_distance_field[neighbor[0]][neighbor[1]] < safest_distance:
                safest_distance = zombie_distance_field[neighbor[0]][neighbor[1]]
                safest_location = neighbor
        print("neighbor:", neighbor)
