__author__ = 'Rafeh'


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

def number_of_threes(num):
    if str(num) == '':
        return 0
