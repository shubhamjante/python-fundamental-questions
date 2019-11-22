"""
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding.
Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run
length encoded String.

Provide different String values and test your program

========================================
| Sample Input      | Expected Output   |
========================================
| AAAABBBBCCCCCCCC  | 4A4B8C            |
| AABCCA            | 2A1B2C1A          |
========================================
"""


def encode(message):
    # Remove pass and write your logic here
    encoded = ""
    message += " "
    counter = 1
    character = message[0]

    for i in range(1, len(message)):
        if character == message[i]:
            counter = counter + 1

        else:
            encoded += str(counter) + character
            character = message[i]
            counter = 1
    return encoded


encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)