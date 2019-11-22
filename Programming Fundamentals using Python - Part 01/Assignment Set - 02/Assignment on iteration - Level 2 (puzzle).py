"""
Write a python program to solve a classic ancient Chinese puzzle.

We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

=============================================
| Sample Input          | Expected Output   |
=============================================
| heads-150 legs-400    | 100 50            |
| heads-3 legs-11       | No solution       |
| heads-3 legs-12       | 0 3               |
| heads-5 legs-10       | 5 0               |
=============================================
"""


def solve(heads, legs):
    error_msg = "No solution"

    rabbit_count = (legs - (2 * heads))/2
    chicken_count = heads - rabbit_count
    if rabbit_count >= 0 and chicken_count >= 0 and rabbit_count == int(rabbit_count) and chicken_count == int(chicken_count):
        print(int(chicken_count), int(rabbit_count))
    else:
        print(error_msg)


solve(38, 131)