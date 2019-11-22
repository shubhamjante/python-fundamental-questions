"""
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below
and returns the encrypted message.

Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order
should not change

Note:
Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.

=========================================================
| Sample Input              | Expected Output           |
=========================================================
| the sun rises in the east | eht snu sesir ni eht stea |
=========================================================
"""


def encrypt_sentence(sentence):
    li = sentence.split(" ")
    new = ""
    vowel = ["a" , "e", "i", "o", "u"]

    for i in range (0, len(li)):
        if i % 2 == 0:
            temp = li[i][::-1]
            new += temp + " "
        else:
            temp2 = ""
            s = ""
            for alpha in li[i]:
                if alpha.lower() in vowel:
                    s += alpha
                else:
                    temp2 += alpha
            new += temp2 + s + " "
    new = new[:-1]
    return new


sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)