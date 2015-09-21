def prime_checker(number):
 if number == 2:
  return True
 for i in range(2, number//2+1):
  if number%i == 0:
   return False
 return True

def largest_prime_factor(number):
 for i in range(2, number//2+1)[::-1]:
  if number % i == 0:
   if prime_checker(i):
    return i
 return False

print(largest_prime_factor(600851475143))
