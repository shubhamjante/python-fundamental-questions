"""
You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z.
The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins.
How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.

=====================================================================
| Sample Input                          | Expected Output           |
=====================================================================
| Available   | Available   | Amount to | Rs. 1 coins | Rs. 5 notes |
| Rs. 1 coins | Rs. 5 Notes | be made   | needed      | needed      |
=====================================================================
| 2           | 4           | 21        | 1           | 4           |
---------------------------------------------------------------------
| 11          | 2           | 11        | 1           | 2           |
---------------------------------------------------------------------
| 3           | 3           | 19        | -1                        |
=====================================================================
"""


def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = rupees_to_make // 5
    one_needed = rupees_to_make - (five_needed * 5)

    # if (5 * no_of_five + no_of_one) != rupees_to_make:
    #     print(-1)
    if five_needed > no_of_five or one_needed > no_of_one:
        print(-1)
    else:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)


make_amount(28, 8, 5)