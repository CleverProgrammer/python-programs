def prime(x):
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def thou_first_prime(user_input):
    number = 1
    prime_counter = 0
    while 1:
        number+=1
        if prime(number):
            prime_counter += 1
            if prime_counter == user_input:
                return number
            
print("answer: %s" %thou_first_prime(10001))

