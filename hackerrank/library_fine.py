# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 03:36:28 2015

@author: Rafeh
"""
from collections import namedtuple


def fee(book_return_date, book_due_date):

    '''
    Take book return date and book due date as input, return the fine.
    >>> fee('9 9 2015', '6 9 2015')
    45
    >>> fee('9 9 2015', '6 9 2013')
    10000
    >>> fee('9 9 2015', '6 8 2015')
    500
    >>> fee('9 9 2015', '9 9 2015')
    0
    >>> fee('9 9 2015', '6 7 2015')
    1000
    >>> fee('9 9 2015', '6 11 2014')
    10000
    >>> fee('28 2 2015', '15 4 2015')
    0
    '''
    Date = namedtuple('Date', ['day', 'month', 'year'])
    due = Date(*map(int, book_due_date.split()))
    book_return = Date(*map(int, book_return_date.split()))

    if book_return.year > due.year:
        fine = 10000

    elif book_return.year < due.year:
        fine = 0

    elif book_return.month > due.month:
        fine = 500 * (book_return.month - due.month)

    elif book_return.month < due.month:
        fine = 0

    elif book_return.day > due.day:
        fine = 15 * (book_return.day - due.day)

    elif book_return.day < due.day:
        fine = 0

    else:
        fine = 0

    return fine


if __name__ == '__main__':
    import doctest
    doctest.testmod()
