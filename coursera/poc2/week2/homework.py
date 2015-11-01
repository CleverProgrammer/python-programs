"""
Question 6: Recursive Permutation.
"""
def permutations(word):
    """
    Algorithm Recurrence Relation: n!
    :param word: string or list
    :return: list
    """
    if len(word) == 0:
        return ['']

    perms = permutations(word[1:])
    result = []
    for perm in perms:
        for pos in range(len(perm)+1):
            result.append(perm[:pos] + word[0] + perm[pos:])
    return result


def memoized_fib(num, memo_dict):
    """
    Algorithm Recurrence Relation: 2n-1
    :param num: number
    :param memo_dict: dictionary, not user input.
    :return: number
    """
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

