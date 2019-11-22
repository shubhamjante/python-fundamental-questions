"""
Write a python program to display all the common characters between two strings.
Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

=========================================================
| Sample Input                      | Expected Output   |
=========================================================
| "I like Python"                   | lieyon            |
| "Java is a very popular language" |                   |
=========================================================
"""


def find_common_characters(msg1, msg2):
    common = ''
    for char in msg1:
        if char in msg2 and char.isalpha() and char not in common:
            common += char

    if not len(common):
        return -1
    else:
        return common


msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
