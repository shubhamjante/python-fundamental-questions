"""
Write a python function, nearest_palindrome() which accepts a number and returns the nearest
palindrome greater than the given number.

=====================================
| Sample Input  | Expected Output   |
=====================================
| 12300         | 12321             |
| 12331         | 12421             |
=====================================
"""


def reverse(number):
    return  int(''.join(list(str(number)[::-1])))


def nearest_palindrome(number):
    if number == reverse(number):
        return number
    else:
        while True:
            number += 1
            if number == reverse(number):
                return number


number = 12300
print(nearest_palindrome(number))
