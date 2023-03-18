# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n % 2 == 0: return False
  if n < 9: return True
  if n % 3 == 0: return False
  
  # Primes have prime factorization of itself and 1,
  # so, to determine if n itself is prime,
  # we only need to check if other primes <= sqrt(n) are factors of n.
  #
  # Since all primes > 3 are of the form 6n ± 1 (Euler's 6n=1 theorem),
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6.

  r = int(n**0.5) 
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

n = 600851475143
r = int(n**0.5)
primes = []

for i in range(r, 1, -1):
    if is_prime(i) and n % i == 0:
        primes.append(i)
print(primes)