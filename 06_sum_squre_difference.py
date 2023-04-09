# Problem 6
# The sum of the squares of the first ten natural numbers is,
#   1 + 4 + 9 + 16 + ... + 100 = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
#   3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def square(list):
    return [i ** 2 for i in list]

n = 100
sumOfSquare = sum(square(range(n + 1)))
squareOfSum = sum(range(n + 1)) ** 2
difference = squareOfSum - sumOfSquare

print(difference)

