"""
Greedy Boss Simulator
Simulator for greedy boss scenario
"""
import unittest
# import simpleplot
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
    Takes as input the number of days in the simulation (an integer) and the amount by which the boss increases the cost
    of a bribe after each bribe (an integer). The final parameter has either the constant value STANDARD or LOGLOG and
    specifies whether the returned list is either in standard scale or log/log scale.
    The function greedy_boss() should return the list days_vs_earnings
    Subsequent tuples added to this list should consist of the day when a bribe takes place and the total salary earned up to
    and including that day. This total salary earned should include money spent on the current day's bribe as well as all
    previous bribes.
    """
    # if bribe:
        # days_vs_earnings.append( (current_day, current_total_salary+all_bribes))

    # initialize necessary local variables
    current_bribe_cost = INITIAL_BRIBE_COST  # next bribe cost
    current_day = 0  # how much time has passed
    total_salary = 0  # how much I have earned in total
    current_salary = INITIAL_SALARY  # earnings each day
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        print("current_bribe_cost: %s" % str(current_bribe_cost))
        current_salary += SALARY_INCREMENT
        print(current_salary)

        # check whether we have enough total_salary to bribe without waiting
        if current_salary > current_bribe_cost:
            days_vs_earnings.append((current_bribe_cost / SALARY_INCREMENT, current_salary))
            

        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
            current_day = days_vs_earnings[-1][0]
        print("days_vs_earnings[-1]: %s" % str(days_vs_earnings[-1]))
        print("current_day: %s" % str(current_day))
        print("total_salary: %s" % str(total_salary))
        # update state of simulation to reflect bribe

        # update list with days vs total salary earned for most recent bribe
        # use plot_type to control whether regular or log/log plot
    return days_vs_earnings


def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = STANDARD
    days = 70
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings",
                          [inc_0, inc_500, inc_1000, inc_2000], False,
                          ["Bribe increment = 0", "Bribe increment = 500",
                              "Bribe increment = 1000", "Bribe increment = 2000"])

# run_simulations()

# print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

# print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000),
# (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300),
# (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35,
# 16900)]


class GreedyBoss(unittest.TestCase):

    def test_greedy_boss(self):
        computed = greedy_boss(35, 100)
        expected = [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]
        self.assertEqual(computed, expected)

suite = unittest.TestLoader().loadTestsFromTestCase(GreedyBoss)
unittest.TextTestRunner(verbosity=0).run(suite)
