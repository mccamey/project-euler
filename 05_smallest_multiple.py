# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
# without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple():
    primes = [2, 3, 5, 7, 11, 13, 17, 19] # list of prime factors
    factors = []
    exponent = []
    for p in primes:
        factor = p
        while factor <= 20:
            factor *= p
        factor //= p
        factors.append(factor)
        print(factors)
    return (2**4) * (3**2) * (5**1) * (7**1) * factors[0] * factors[1] * factors[2] * factors[3]

print(smallest_multiple())