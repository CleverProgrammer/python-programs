import random


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name


# noinspection PyMethodMayBeStatic
class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)
