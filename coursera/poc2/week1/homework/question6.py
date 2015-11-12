__author__ = 'ChessTastic'


"""
Question 6: Recursive Permutations
"""

def permutations(outcomes):
    # base case
    if not outcomes:
        return set()

    # recursive case
    rest_permutations = outcomes[1:]
    for pos, perm in enumerate(rest_permutations):
        pass

# print(permutations([1,2,3,4]))
set_ = set()
set_.add((1,2,1,2))
set_.add((1,2,2,1))
set_.add((2,3,3,3))
set_.add((2,1,1,3))
set_.add(('h','h','e',))
print(set_)