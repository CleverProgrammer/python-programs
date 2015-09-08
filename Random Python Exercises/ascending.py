def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(1,len(numbers)):
        if numbers[i+1] < numbers[i]:
            return False
    return True

print (is_ascending([2, 6, 9, 12, 400]))
