"""
Author: Rafeh Qazi
Program: Simulator for greedy boss scenario
Class: Coursera POC 1 Week 5
Date: 10/03/2015
Link: http://www.codeskulptor.org/#user40_hEhvJIG1CB_2.py
Graph Link: http://www.codeskulptor.org/#user40_hEhvJIG1CB_15.py
Coursera Imports: https://class.coursera.org/principlescomputing1-004/wiki/=view?page=imports
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
    Simulation of greedy boss
    """

    # initialize necessary local variables
    current_day = 0
    current_salary = INITIAL_SALARY
    total_salary = 0
    current_bribe_cost = INITIAL_BRIBE_COST
    current_money = 0
    days_till_next_bribe = 0
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        days_till_next_bribe = math.ceil((current_bribe_cost - current_money) / current_salary)
        current_day += days_till_next_bribe
        current_money += current_salary * days_till_next_bribe
        total_salary += current_salary * days_till_next_bribe
        # check whether we have enough savings to bribe without waiting
        while current_money >= current_bribe_cost:
            if current_day > days_in_simulation:
                return days_vs_earnings
            current_money -= current_bribe_cost
            if plot_type == STANDARD:
                days_vs_earnings.append((current_day, total_salary))
            else:
                days_vs_earnings.append([math.log(current_day), math.log(total_salary)])
            current_salary += SALARY_INCREMENT
            current_bribe_cost += bribe_cost_increment

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


class GreedyBoss(unittest.TestCase):

    def test_greedy_boss1(self):
        computed = greedy_boss(35, 100)
        expected = [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100),
                    (29, 7900), (31, 9300), (33, 10900), (35, 12700)]
        self.assertEqual(computed, expected)

    def test_greedy_boss2(self):
        computed = greedy_boss(35, 0)
        expected = [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000),
                    (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300),
                    (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
        self.assertEqual(computed, expected)

suite = unittest.TestLoader().loadTestsFromTestCase(GreedyBoss)
unittest.TextTestRunner(verbosity=2).run(suite)
