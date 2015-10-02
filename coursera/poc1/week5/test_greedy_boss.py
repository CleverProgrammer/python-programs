"""
Simulator for greedy boss scenario
"""

# import simpleplot
import unittest
import math
# import codeskulptor
# codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    """
    Simulation of greedy boss
    """

    # initialize necessary local variables
    current_day = 0
    current_salary = INITIAL_SALARY
    total_salary = 0
    current_bribe_cost = INITIAL_BRIBE_COST
    current_money = 0
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        current_day += 1
        current_money += current_salary
        total_salary += current_salary
        if current_money >= current_bribe_cost:
            current_money -= current_bribe_cost  # hand boss $1000
            days_vs_earnings.append((current_day, total_salary))
            current_salary += SALARY_INCREMENT
            current_bribe_cost += bribe_cost_increment
        # check whether we have enough savings to bribe without waiting

        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)

        # update state of simulation to reflect bribe

        # update list with days vs total salary earned for most recent bribe
        # use plot_type to control whether regular or log/log plot

    return days_vs_earnings


class GreedyBoss(unittest.TestCase):

    def test_greedy_boss(self):
        computed = greedy_boss(35, 100)
        expected = [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]
        self.assertEqual(computed, expected)

suite = unittest.TestLoader().loadTestsFromTestCase(GreedyBoss)
unittest.TextTestRunner(verbosity=0).run(suite)
