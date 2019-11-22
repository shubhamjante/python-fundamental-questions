"""
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers.
Assume that the words contain only uppercase letters and the maximum word length is 10.

=================================================================================
| Sample Input                                              | Expected Output   |
=================================================================================
| {"THEIR": "THEIR", "BUSINESS": "BISINESS",                |                   |
| "WINDOWS":"WINDMILL", "WERE":"WEAR", "SAMPLE":"SAMPLE"}   | [2, 2, 1]         |
=================================================================================
"""


def find_correct(word_dict):
    wrong = 0
    almost = 0
    correct = 0
    li = []

    for i, j in word_dict.items():
        if len(i) != len(j):
            wrong += 1
        else:
            mistake_counter = 0
            for x in range(0, len(i)):
                if i[x] == j[x]:
                    continue
                else:
                    mistake_counter += 1

            if mistake_counter == 0:
                correct += 1

            elif mistake_counter <= 2:
                almost += 1

            else:
                wrong += 1

    return [correct, almost, wrong]


word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
