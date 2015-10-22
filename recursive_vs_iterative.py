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

    # recursive case
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
    # base case
    if x == 0:
        return 0

    # recursive case
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
    # base case
    if num == 0:
        return 0

    # recursive case
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
    for i in my_list:
        if i == elem:
            return True
    return False


def recursive_is_member(my_list, elem):
    """
    recursive solution that takes a list and an element as input. It returns True if the elem exists in my_list.
    It returns False if the elem does not exist in my_list.
    :param my_list: list
    :param elem: string or number
    :return: True or False
    """
    # base case
    if not my_list:
        return False  # if there are no elements in the list. Return False.

    # condition
    if my_list[-1] == elem:
        return True

    # recursive case
    return recursive_is_member(my_list[:-1], elem)  # shorten list by removing the last element each time


def iterative_remove_x(my_string):
    """
    iterative solution that takes in a string and returns it with all instances of 'x' removed.
    :param my_string: string
    :return: string
    """
    new_string = ''
    for i in my_string:
        if i is not 'x':
            new_string += i
    return new_string


def recursive_remove_x(my_string):
    """
    iterative solution that takes in a string and returns it with all instances of 'x' removed.
    :param my_string: string
    :return: string
    """
    # base case
    if not my_string:  # check if string is empty
        return ''

    # recursive case
    if my_string[-1] != 'x':
        return recursive_remove_x(my_string[:-1]) + my_string[-1]
    return recursive_remove_x(my_string[:-1])


def iterative_insert_x(my_string):
    """
    iterative recursive solution that takes in a string and returns the string with 'x' added in between every character
    :param my_string: string
    :return: string
    """
    new_string = ''
    for i in my_string[:-1]:
        new_string += i + 'x'
    new_string += my_string[-1]
    return new_string


def recursive_insert_x(my_string):
    """
    recursive solution that takes in a string and returns the string with 'x' added in between every character.
    :param my_string: string
    :return: string
    """
    # base case
    if not my_string:
        return ''

    # base case 2
    if len(my_string) == 1:
        return my_string[0]

    # recursive case
    return recursive_insert_x(my_string[:-1]) + 'x' + my_string[-1]


def iterative_list_reverse(my_list):
    """
    iterative solution that takes in a list and returns the list in a reversed order.
    :param my_list: list
    :return: list
    """
    return my_list[::-1]


def recursive_list_reverse(my_list):
    """
    recursive solution that takes in a list and returns the list in a reversed order.
    :param my_list: list
    :return: list
    """
    # base case
    if not my_list:
        return []

    # recursive case
    return [my_list[-1]] + recursive_list_reverse(my_list[:-1])


def recursive_anagrams(word):
    """
    recursive solution that takes in a word and spits back all the possible permutations of that word.
    :param word: string
    :return: list
    # 'abc'
    # w in 'abc'[1:]
    # w = 'b'
    #     pos in range(len('b') + 1)
    #     pos in range([0, 1])
    #     pos = 0
    #          w[:pos] + 'abc'[0] + w[pos:]
    #          ''      + 'a'      + 'bc'
    """
    if not word:
        return ['']
    else:
        ans = []
        for ch in recursive_anagrams(word[1:]):
            for pos in range(len(ch) + 1):
                ans.append(ch[:pos] + word[0] + ch[pos:])
        return ans


def iterative_exponents(number, power):
    """
    iterative solution that takes a number and an its exponent power and returns its result.
    :param number: number
    :param power: number
    :return: number
    """
    result = 1
    for _ in range(power):
        result *= number
    return result

def recursive_exponents(number, power):
    """
    recursive iterative solution that takes a number and an its exponent power and returns its result.
    :param number: number
    :param power: number
    :return: number
    """
    # 2^8  ==> 2^4  ==> 2^2 ==> 2*2
    # 2*2 = 4 ==> 4*4 = 16 ==> 16*16 = 256

    # base case
    if power == 0:
        return 1

    # recursive case
    else:
        factor = recursive_exponents(number, power//2)
        if power%2 == 0:
            return factor * factor
        else:
            return factor * factor * number


def recursive_fibonacci(n):
    """
    recursive solution that takes an nth term and returns its fibonacci value
    :param number: number
    :return: number
    """
    # base case
    if n in (0, 1, 2):
        return 1

    # recursive case
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def recursive_gcd(num1, num2):
    """
    recursive solution that takes in two numbers and returns their greatest common divisor
    :param num1: number
    :param num2: number
    :return: number
    """
    pass
    pass
