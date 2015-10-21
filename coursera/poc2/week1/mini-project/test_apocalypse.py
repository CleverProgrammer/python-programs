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
        state = Apocalypse(5, 5, zombie_list = [(1,2), (2,3)], human_list = [(0,0), (4,4)])
        zombie_distance_field = state.compute_distance_field(zombie_apocalypse_bfs.ZOMBIE)
        print()
        print("-------------------------------")
        print("Zombie Distance Field:")
        for row in zombie_distance_field:
            print(row)
        print()
        # new_human_list is going to be used later to create a new_list with new and safer human coordinates
        new_human_list = []

        human_generator = state.humans()
        human = next(human_generator)
        self.assertEqual(human, (0,0), "test human generator")
        neighbors = state.eight_neighbors(human[0], human[1])
        print("neighbors:", neighbors)
        self.assertEqual(neighbors, [(1, 0), (0, 1), (1, 1)], "testing human's neighbors")
        human_distance = zombie_distance_field[human[0]][human[1]]
        farthest_distance = human_distance  #initialized as human_distance until it finds a farther distance from zombie
        safest_location = human  # initialized as human until it finds a better coordinate on the grid

        # Check all the neighbors to find the safest location for the human based on the farthest distance from zombie
        for neighbor in neighbors:
            print(neighbor)
            print(zombie_distance_field[neighbor[0]][neighbor[1]])
            if zombie_distance_field[neighbor[0]][neighbor[1]] > farthest_distance:
                farthest_distance = zombie_distance_field[neighbor[0]][neighbor[1]]  # distance value
                safest_location = neighbor  # coordinate (row, col)
        self.assertEqual(safest_location, (0,0), "test safest_location for move_human function")

        # now that the safest new location for the human has been chosen after analyzing each neighbor, let's add that
        # to the new_human_list. self._human_list is going to get replaced by this one at the end
        new_human_list.append(safest_location)
        self.assertEqual(new_human_list, [(0,0)], "test new_human_list that is safer than the original one")

        # ---- Sample Owl Test for move_human method ----
        obj = Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
        print((1,1) in obj._human_list)
        dist = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
        obj.move_humans(dist)
        self.assertEqual(obj._human_list, [(0,0)], "test new_human list")

        # ---- Sample Owl Test for move_human method ----
        obj = Apocalypse(3, 3, [(0, 0), (0, 1), (0, 2), (1, 0)], [(2, 1)], [(1, 1)])
        dist = [[9, 9, 9], [9, 1, 2], [1, 0, 1]]
        obj.move_humans(dist)
        self.assertEqual(obj._human_list, [(1, 2)], "test updated human list")

    def test_move_zombie(self):
        obj = Apocalypse(3, 3, [(1, 1), (1, 2)], [(2, 2)], [(0, 2)])
        dist = [[2, 1, 0], [3, 9, 9], [4, 5, 6]]
        obj.move_zombies(dist)
        self.assertEqual(obj._zombie_list, [(2, 1)], "test updated zombie list")
