"""
Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9.
Otherwise it should return false.

The length of the list can be less than 4 also.

=========================================
| Sample Input      | Expected Output   |
=========================================
| [1, 2, 9, 3, 4]   | True              |
| [1, 2, 9]         | True              |
| [1, 2,3,4]        | False             |
=========================================
"""


def find_nine(nums):
    li = nums[:4]
    if li.count(9) >= 1:
        return True
    else:
        return False


nums = [1, 9, 4, 5, 6]
print(find_nine(nums))
