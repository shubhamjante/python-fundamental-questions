"""
Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from
the given string and return it.

=================================================
| Sample Input                  | Output        |
=================================================
| 1122334455ababzzz@@@123#*#*   | 12345abz@#*   |
=================================================
"""


def remove_duplicates(value):
    data = list()
    for char in value:
        if char not in data:
            data.append(char)

    return ''.join(data)


print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
