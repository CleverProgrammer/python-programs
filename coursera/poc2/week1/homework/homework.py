"""
Question 6: Recursive Permutation.
"""

def permutations(word):
    if len(word) == 0:
        return ['']

    perms = permutations(word[1:])
    result = []
    for perm in perms:
        for pos in range(len(perm)+1):
            result.append(perm[:pos] + word[0] + perm[pos:])
    return result


print(permutations("hello"))