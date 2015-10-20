__author__ = 'Rafeh'
"""
Program: recursive_vs_iterative

Description: This program contains a few common iterative functions and their solutions. More importantly,
it also contains their counter-part recursive functions and their solutions. This is important in visualizing
side by side the differences between iterative implementations and recursive implementations of a given function.
Notice that recursive solutions tend to be more elegant!

Version: 3.4
"""

def iterative_double(x):
    """
    iterative function that doubles the input
    :param x: number
    :return: double the number
    """
    return x * 2


def recursive_double(x):
    """
    recursive function that doubles the input
    :param x: number
    :return: double the number
    """
    # base case
    if x == 0:
        return 0
    return recursive_double(x - 1) + 2  # double every number


def iterative_sum_up_to(x):
    """
    iterative solution that takes an input x and sums all the way up to x and returns the summed up value
    :param x: number
    :return: number that is summed up to x
    """
    summer = 0
    for i in range(x + 1):
        summer += i
    return summer


def recursive_sum_up_to(x):
    """
    recursive solution that takes an input x and sums all the way up to x and returns the summed up value
    :param x: number
    :return: number that is summed up to x
    """
    if x == 0:
        return 0
    return recursive_sum_up_to(x - 1) + x


def iterative_number_of_threes(num):
    """
    iterative solution that takes an input num and returns how many times the digit 3 occurred.
    :param num: number
    :return: number of times 3 occurred
    """
    three = 0
    for i in str(num):
        if i == str(3):
            three += 1
    return three


def recursive_number_of_threes(num):
    """
    recursive solution that takes an input num and returns how many times the digit 3 occurred.
    I am going to use a neat little divide number by 10 technique to get the last digit.
    :param num: number
    :return: number of times 3 occurred
    """
    if num == 0:
        return 0
    if num % 10 == 3:
        return recursive_number_of_threes(num // 10) + 1  # if last digit is three then add 1
    return recursive_number_of_threes(num // 10)  # if last digit is three then add 0

def iterative_is_member(my_list, elem):
    """
    iterative solution that takes a list and an element as input. It returns True if the elem exists in my_list.
    It returns False if the elem does not exist in my_list.
    :param my_list: list
    :param elem: string or number
    :return: True or False
    """
