def prime(x):
 for i in range(2, x):
  if x % i == 0:
   return False
 return True

def thou_first_prime(input):
    number = 1
    prime_counter = 0
    while 1:
        number+=1
        if prime(number):
            prime_counter += 1
            if prime_counter == input:
                return number

