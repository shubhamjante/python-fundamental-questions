"""
Write a python function to create and return a new dictionary from the given dictionary(item:price).

Given the following input, create a new dictionary with elements having price more than 200.

prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}

=================================================================================
| Sample Input                              | Expected Output                   |
=================================================================================
| { 'ACME': 45.23,'AAPL': 612.78,           | {'AAPL': 612.78,                  |
| 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}   | 'IBM': 205.55}                    |
---------------------------------------------------------------------------------
| { 'MANGO': 150.45,'POMOGRANATE': 250.67,  | {'ORANGE': 200.75,                |
| 'BANANA': 20.55,'CHERRY': 500.10,         | 'CHERRY': 500.1,                  |
| 'ORANGE': 200.75}                         | 'POMOGRANATE': 250.67}            |
=================================================================================
"""


def create_new_dictionary(prices):
    new_dict = {}

    for key, value in prices.items():
        if value > 200:
            new_dict[key] = value

    return new_dict


prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
print(create_new_dictionary(prices))
