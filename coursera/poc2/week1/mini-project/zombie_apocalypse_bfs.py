__author__ = 'Rafeh'

"""
http://www.codeskulptor.org/#user40_HFYBBvbkJb_8.py
Student portion of Zombie Apocalypse mini-project
"""

import poc_grid
import poc_queue
import math
# import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of zombie on grid with
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
        else:
            self._obstacle_list = []
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
        Reset zombie and zombie lists to be empty
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
        Add zombie to the zombie list
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
        for zombie in self._human_list:
            yield zombie

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
        distance_field =[[self._grid_height * self._grid_width for dummy_col in range(self._grid_width)]
                         for dummy_row in range(self._grid_height)]

        # grid visited is initialized to be empty
        visited = poc_grid.Grid(self._height, self._width)
        for row, col in self.obstacle():
            visited.set_full(row, col)

        # initializing boundary queue and the humans_or_zombies list type.
        boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            humans_or_zombies = self._zombie_list
        elif entity_type == HUMAN:
            humans_or_zombies = self._human_list
        else:
            return  # should return nothing if entity_type is None

        # Update boundary and mark each human_or_zombie (row, col) tuple as visited. Also, set the human_or_zombie
        # tuple to be zero on the distance field grid.
        for human_or_zombie in humans_or_zombies:
            boundary.enqueue(human_or_zombie)
            visited.set_full(human_or_zombie[0], human_or_zombie[1])
            distance_field[human_or_zombie[0]][human_or_zombie[1]] = 0

        while boundary:
            current_cell = boundary.dequeue()
            neighbors = visited.four_neighbors(current_cell[0], current_cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]):  # can't use `not in` because no such method
                    visited.set_full(neighbor[0], neighbor[1])  # add neighbor cell to visited
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
                    boundary.enqueue(neighbor)


        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_human_list = []
        for zombie in self.humans():
            neighbors = self.eight_neighbors(zombie[0], zombie[1])
            human_distance = zombie_distance_field[zombie[0]][zombie[1]]
            farthest_distance = human_distance  #initialized as human_distance until it finds a farther distance from zombie
            safest_location = zombie  # initialized as zombie until it finds a better coordinate on the grid
            for neighbor in neighbors:
                if neighbor in self._obstacle_list:
                    continue
                if zombie_distance_field[neighbor[0]][neighbor[1]] > farthest_distance:
                    farthest_distance = zombie_distance_field[neighbor[0]][neighbor[1]]  # distance value
                    safest_location = neighbor  # coordinate (row, col)
            new_human_list.append(safest_location)

        self._human_list = new_human_list

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_zombie_list = []
        for zombie in self.zombies():
            neighbors = self.four_neighbors(zombie[0], zombie[1])
            zombie_distance = human_distance_field[zombie[0]][zombie[1]]
            farthest_distance = zombie_distance  #initialized as human_distance until it finds a farther distance from zombie
            safest_location = zombie  # initialized as zombie until it finds a better coordinate on the grid
            for neighbor in neighbors:
                if neighbor in self._obstacle_list:
                    continue
                if human_distance_field[neighbor[0]][neighbor[1]] < farthest_distance:
                    farthest_distance = human_distance_field[neighbor[0]][neighbor[1]]  # distance value
                    safest_location = neighbor  # coordinate (row, col)
            new_zombie_list.append(safest_location)

        self._zombie_list = new_zombie_list


# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))
