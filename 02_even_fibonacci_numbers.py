# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a1 = 1
a2 = 2
an = a1 + a2
sum = 2

while a2 <= 4000000:
    a1 = a2
    a2 = an
    an = a1 + a2
    if an % 2 == 0:
        sum += an
print(sum)