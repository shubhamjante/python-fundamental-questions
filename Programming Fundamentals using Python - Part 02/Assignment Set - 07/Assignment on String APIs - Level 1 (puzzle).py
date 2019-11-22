"""
Write a python function, check_anagram() which accepts two strings and returns True,
if one string is a special anagram of another string. Otherwise returns False.

The two strings are considered to be a special anagram if they contain repeating characters
but none of the characters repeat at the same position. The length of the strings should be the same.

Note: Perform case insensitive comparison wherever applicable.

=============================================================================================================
| Sample Input          | Expected Output   | Description                                                   |
=============================================================================================================
| eat, tea              | True              |                                                               |
| backward,drawback     | False             | (Reason: character 'a' repeats at position 6, not an anagram) |
| Reductions,discounter | True              |                                                               |
| About, table          | False             |                                                               |
=============================================================================================================
"""


def check_anagram(data1, data2):
    count = 0
    data1 = data1.lower()
    data2 = data2.lower()

    if len(data1) != len(data2):
        return False

    for i, char in enumerate(data1):
        if data1[i] == data2[i]:
            return False
        elif char in data2:
            count += 1

    if count == len(data1):
        return True
    else:
        return False


def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


print(check_anagram("About", "table"))
