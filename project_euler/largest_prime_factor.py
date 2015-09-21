def prime(number):
 if number in [2, 3, 5, 7]:
  return True
 elif number%2 == 0:
  return False
 else:
  for i in range(2, number//4+1, 2):
   if number%i == 0:
    return False
 return True

def largest_prime_factor(number):
 if prime(number//2):
  return True
 else:
  for i in range(2, number//4+1)[::-1]:
   if number % i == 0:
    if prime(i):
     return i
 return False

print(prime(786))
print(largest_prime_factor(13195))
print(largest_prime_factor(200000))
print(largest_prime_factor(600851475143))
