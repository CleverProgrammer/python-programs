def factorial_(number):
    """
    >>> factorial_(5)
    120
    """
    import math
    return math.factorial(number)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

print(5)
