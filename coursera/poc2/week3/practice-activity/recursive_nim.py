#!/usr/bin/python3
"""
Author: Rafeh Qazi
Date: 11/01/2015
Course:https://class.coursera.org/principlescomputing2-004/wiki/view?page=nim_ts
Lecture: https://class.coursera.org/principlescomputing2-004/lecture/83
Game Description: http://en.wikipedia.org/wiki/Nim#The_21_game
A recursive solver for the game NIM
"""
# import functools


MAX_REMOVE = 3

# recursive solver with no memoization

# how to memoize a function in python3 with decorators


# @functools.lru_cache(None)
def evaluate_position(current_num):
    """
    Recursive solver for Nim
    """
    global counter
    counter += 1
    # base case
    if not current_num:
        # that means your opponent took the last item, not you.
        return "lost"
    for remove in range(1, MAX_REMOVE+1):
        # if we take 1 and our opp loses, we win.
        if evaluate_position(current_num - remove) == "lost":
            return "won", remove
    return "lost"


def run_standard(items):
    """
    Encapsulate code to run regular recursive solver
    """
    global counter
    counter = 0
    print()
    print("Standard recursive version")
    print("Position with", items, "items is", evaluate_position(items))
    print("Evaluated in", counter, "calls")

# run_standard(21)


# memoized version with dictionary

def evaluate_memo_position(current_num, memo_dict):
    """
    Memoized version of evaluate_position
    memo_dict is a dictionary that stores previously computed results
    >>> evaluate_memo_position(21, {0: 'lost'})
    'won'
    >>> evaluate_memo_position(20, {0: 'lost'})
    'lost'
    >>> evaluate_memo_position(3, {0: 'lost'})
    'won'
    >>> evaluate_memo_position(1, {0: 'lost'})
    'won'
    >>> evaluate_memo_position(4, {0: 'lost'}) # mult of 4 should lose
    'lost'
    >>> evaluate_memo_position(2, {0: 'lost'})
    'won'
    >>> evaluate_memo_position(0, {0: 'lost'})
    'lost'
    >>> evaluate_memo_position(8, {0: 'lost'}) # mult of 4 should lose
    'lost'
    >>> evaluate_memo_position(12, {0: 'lost'}) # mult of 4 should lose
    'lost'
    """
    # if someone passed in 0
    if not current_num:
        return 'lost'

    global counter
    counter += 1
    for remove in range(1, MAX_REMOVE+1):
        # check if the result of the following move is already in dictionary
        if current_num - remove in memo_dict:
            # check if it is a lost position for the opponent
            if memo_dict[current_num - remove] == 'lost':
                # set it to a win for us in the future
                memo_dict[current_num] = 'won'
                return 'won'

        elif evaluate_memo_position(current_num - remove, memo_dict) == 'lost':
            memo_dict[current_num] = 'won'
            return 'won'

    memo_dict[current_num] = 'lost'
    return "lost"


def run_memoized(items):
    """
    Run the memoized version of the solver
    """
    global counter
    counter = 0
    print()
    print("Memoized version")
    print("Position with", items, "items is",
          evaluate_memo_position(items, {0: "lost"}))
    print("Evaluated in", counter, "calls")

run_memoized(21)

# counter = 0


# memoized fibonacci for practice
# simply memorize the function calls each time in the dict so you don't have to
# remember them later!
# def fib(n, known={}):
#     global counter
#     counter += 1
#     if n in known:
#         return known[n]
#     if n in (0, 1):
#         return n
#     value = fib(n-1) + fib(n-2)
#     known[n] = value
#     return value
#
# print(map(fib, list(range(5000))))
# print(fib(500))
# print(counter)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
