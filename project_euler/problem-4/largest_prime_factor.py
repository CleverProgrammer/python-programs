#import cProfile


def is_prime(number):
    for i in range(2, number // 4 + 1):
        if number % i == 0:
            return False
    return True


def largest_prime_factor(number):
    if is_prime(number // 2):
        return number // 2
    else:
        for i in range(2, number // 4 + 1)[::-1]:
            if number % i == 0:
                if is_prime(i):
                    return i
    return None


#(is_prime(786))
# largest_prime_factor(2477238317)
# print(largest_prime_factor(200000))
# print(largest_prime_factor(600851475143))
