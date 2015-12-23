# Program that creates a union of lists and returns them after omitting
# duplicates.


def unite(arr1, arr2, arr3):
    """
    >>> unite([1, 2, 3], [6, 4, 3], [2, 6, 2, 7, 9])
    [1, 2, 3, 6, 4, 7, 9]
    """
    united_list = arr1
    for num in arr2:
        if num not in united_list:
            united_list.append(num)
    for num in arr3:
        if num not in united_list:
            united_list.append(num)
    return united_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
