__author__ = 'Rafeh'

"""
Student portion of Zombie Apocalypse mini-project
"""

import unittest
import random
import poc_grid
import poc_queue
# import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


# print(poc_grid.Grid(5,5))
# grid = poc_grid.Grid(5,5)
# print(grid.eight_neighbors(2,1))
# grid.clear()
# print(grid)
class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        self._height = grid_height
        self._width = grid_width
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
            self._obstacle_list = obstacle_list
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._zombie_list = []
        self._human_list = []
        poc_grid.Grid.clear(self)

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human

    def obstacle(self):
        '''
        generator that yields the list of obstacles
        '''
        for obstacle in self._obstacle_list:
            yield obstacle

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # same size as grid but initialized with impossibly high values
        self.distance_field = [[self._height * self._width] * self._width for dummy_idx in range(self._width)]

        # grid visited is initialized to be empty
        self.visited = poc_grid.Grid(self._height, self._width)
        for row, col in self._obstacle_list:
            self.visited.set_full(row, col)

        # initializing boundary queue and the humans_or_zombies_list list type.
        self.boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            humans_or_zombies_list = self._zombie_list
        elif entity_type == HUMAN:
            humans_or_zombies_list = self._human_list

        # mark obstacles as impassible in visited



        self.hold_distance_field = poc_grid.Grid(self._height, self._width)
        for row, col in self._zombie_list:
            self.hold_distance_field.set_full(row, col)

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        pass

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        pass


# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))

def print_stuff():
    apocalypse = Apocalypse(5, 5, [(1, 1), (1, 2)], [(1, 4), (2, 4)])
    # obj.clear()
    print(apocalypse)
    print(apocalypse._zombie_list)
    apocalypse.clear()
    print("\n\n%s" % str(apocalypse))
    print(apocalypse._zombie_list)

    print("--------------adding zombies----------------------")
    apocalypse = Apocalypse(5, 5, [(1, 1), (1, 2)], [(1, 4), (2, 4)], )
    apocalypse.add_zombie(3, 4)
    print(apocalypse._zombie_list)
    print(apocalypse.num_zombies())
    apocalypse.add_human(3, 1)
    print(apocalypse.num_humans())
    print("\n\n")
    zombie_gen = apocalypse.zombies()
    print(next(zombie_gen))
    print(next(zombie_gen))

    # ------- human generator --------
    apocalypse.add_human(3, 3)
    apocalypse.add_human(3, 2)
    human_gen = apocalypse.humans()
    print(next(human_gen))
    print(next(human_gen))


# ------ checking BFS ---------
def print_zombies_grid_but_human_distance_field():
    """
    Just used to scope out the random print statements and put them all in one place
    :rtype : printed objects
    """
    apocalypse = Apocalypse(5, 5)
    zombies = [(random.randrange(0, 5), random.randrange(0, 5)) for i in range(10)]
    for row, col in zombies:
        apocalypse.add_zombie(row, col)
    print(apocalypse._zombie_list)
    print(apocalypse._zombie_list[0][0])
    apocalypse.compute_distance_field('anything can go here for now')
    print(apocalypse.hold_distance_field)
    print("My hold_distance_field four neighbors:", apocalypse.hold_distance_field.four_neighbors(0, 0))
    print("My eight neighbors:", apocalypse.eight_neighbors(0, 0))
    print("Visited: \n%s" % str(apocalypse.visited))
    print(apocalypse.distance_field)


print_zombies_grid_but_human_distance_field()
