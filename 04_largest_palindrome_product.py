# Problem 4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindromic(num):
    # Using list comprehension
    # to convert number to list of integers
    digits = [int(x) for x in str(num)]
    
    for i in range(0 , int(len(digits)/2) + 1):
        if digits[i] != digits[len(digits) - i - 1]:
            return False
    return True

x1 = 100; x2 = 100; xn = 1000;
palindromes = []

for i in range(x1, xn):
    for j in range(x2, xn):
        num = i * j
        if isPalindromic(num):
            palindromes.append(num)
print(max(palindromes))