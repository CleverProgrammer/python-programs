"""
 -*- coding: utf-8 -*-
@Date    : 2015-10-05 01:28:26
@Author  : Rafeh Qazi (rafehqazi1@gmail.com)
@Link    : http://www.codeskulptor.org/#user40_z5Pd9GiYA8_2.py
Cookie Clicker Simulator
"""

import user40_lbarkGzPKK_6 as cookie_clicker_tests 
import simpleplot
import math
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

# -----------------------------------ClickerState Class-------------------------------------------


class ClickerState:

    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self.total_cookies = 0.0
        self.current_cookies = 0.0
        self.current_seconds = 0.0
        self.current_cps = 1.0
        self.history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        history_dict = {'total_cookies': self.total_cookies,
                        'current_cookies': self.current_cookies,
                        'current_seconds': self.current_seconds,
                        'current_cps': self.current_cps}
        string = "\n----------------------------\n"
        for name, item in history_dict.items():
            space_length = 28 - len(str(name) + ": " + str(item))
            string += str(name) + ": " + str(item) + "|".rjust(space_length) + "\n"
        return string + "----------------------------"

    # def print_history(self):
    #    pass

    def get_total_cookies(self):
        """
        Return current number of total_cookies 
        (not total number of total_cookies)

        Should return a float
        """
        return self.current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.current_cps

    def get_time(self):
        """
        Get current time
        
        Should return a float
        """
        return self.current_seconds

    def get_history(self):
        """
        Return history list
        History list should be a list of tuples of the form:
        (time, item, cost of item, total total_cookies)
        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        history_copy = self.history[:]
        return history_copy

    def time_until(self, total_cookies):
        """
        Return time until you have the given number of total_cookies
        (could be 0.0 if you already have enough total_cookies)

        Should return a float with no fractional part
        """
        return math.ceil(total_cookies / self.current_cps)

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        
        pass

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state
        Should do nothing if you cannot afford the item
        """
        item = (self.current_seconds, item_name, cost, self.total_cookies)
        self.current_cookies -= cost
        self.current_cps += additional_cps
        self.history.append(item)
        return 

# -----------------------------------Simulation Functions-------------------------------------------


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    return ClickerState()


def strategy_cursor_broken(total_cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(total_cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(total_cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    return None


def strategy_expensive(total_cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    return None


def strategy_best(total_cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print("Chosen Strategy: " + strategy_name.upper() + str(state))

    # Plot total total_cookies over time

    # Uncomment out the lines below to see a plot of total total_cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total total_cookies', [history], True)


def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)


# -----------------------------------PLAYGROUND-------------------------------------------
run()
clicker_state_obj = ClickerState()
clicker_state_obj.buy_item('Grandma', 100, 0.6)
clicker_state_obj.buy_item('Grandma', 115, 0.6)
print(clicker_state_obj.get_history())
x = clicker_state_obj.get_history()
x.append('bullshit')
print(clicker_state_obj.get_history())

obj2 = ClickerState()
print(obj2.time_until(50))

obj = provided.BuildInfo()
obj.clone()
print("build_items: %s" % str(obj.build_items()))
print("Grandma COST: %s" % obj.get_cost('Grandma'))
print("Grandma CPS: %s" % obj.get_cps('Grandma'))
obj.update_item('Grandma')
print("Grandma COST: %s" % obj.get_cost('Grandma'))


# -------------------------------TESTS----------------------------------------
cookie_clicker_tests.run_suite(ClickerState)





# -----------------------------------GREEDYBOSS-------------------------------------------
# Greedy boss function. Need to use later to help in cookie_clicker
def greedy_boss(days_in_simulation, bribe_cost_increment):
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
            days_vs_earnings.append((current_day, total_salary))
            current_salary += SALARY_INCREMENT
            current_bribe_cost += bribe_cost_increment
