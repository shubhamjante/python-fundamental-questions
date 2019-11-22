"""
Use Luhn algorithm to validate a credit card number.

A credit card number has 16 digits, the last digit being the check digit. A credit card number can be validated
using Luhn algorithm as follows:

Step 1a: From the second last digit (inclusive), double the value of every second digit.
Suppose the credit card number is 1456734512345698.
Take the double of 9,5,3,1,4,7,5 and 1
i.e., 18, 10, 6, 2, 8, 14, 10 and 2

Note: If any number is greater than 9, then sum the digits of that number.
i.e., 9, 1, 6, 2, 8, 5 ,1 and 2

Step 1b: Sum the numbers obtained in Step 1a.
i.e., 34

Step 2: Sum the remaining digits in the credit card and add it with the sum from Step 1b.
i.e., 34 + (8+6+4+2+5+3+6+4) = 72

Step 3: If the total is divisible by 10 then the number is valid else it is not valid.

Write a function, validate_credit_card_number(), which accepts a 16 digit credit card number and
returns true if it is valid as per Luhn’s algorithm or false, if it is invalid.
"""


def sum_the_digits(number):
    return sum(map(int, list(str(number))))


def validate_credit_card_number(card_number):
    if len(str(card_number)) != 16:
        return False

    step_1a = list()
    for i in list(map(int, list(str(card_number)[:-1][::-2]))):
        step_1a.append(i+i)

    step_1b = sum([sum_the_digits(num) for num in step_1a])
    step_2 = step_1b + sum(list(map(int, list(str(card_number)[::-2]))))

    if step_2 % 10:
        return False
    else:
        return True


card_number = 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result = validate_credit_card_number(4539869650133101)

if result:
    print("credit card number is valid")
else:
    print("credit card number is invalid")