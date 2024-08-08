"""
258. Add Digits
Easy
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
"""


# Naive solution
def add_digits(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number


print(add_digits(12345))


# Optimized Solution
def add_digits_optimized(number):
    return 0 if number == 0 else (1 + (number - 1) % 9)


print(add_digits_optimized(12345))
