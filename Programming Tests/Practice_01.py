"""
Consider an input_list containing strings.
Each element of the input_list contains strings separated by ":" in the following format –
"<<left_string>> : <<right_string>>"

Write a function which accepts the input_list mentioned above as input parameter and returns an output_list containing
strings. The output_list is created based on following rules:

For each string in the input_list –

* Identify the index position of alphabets in left_string and identify the index position of integers on right_string.
Note: Index starts from 0.
For Example: If the string is 'A12z3:xy9z1' then left_string is 'A12z3' and right_string is 'xy9z1'.
The alphabets in left_string are available at 0 and 3 index positions and the integer digits in right_string
are available at index positions 2 and 4.

* Generate a left index string using the indices obtained from left_string and right index string from the indices
obtained from right_strings.
Concatenate them delimited by ":" to get output_string.

* Add output_string to output_list.
For the above example: The output string will be "03:24".

* If the left_string contains no alphabets add "X" in place of left index string and if the right_string
contains no integer digits add "Y" to the right index string of output_string.
For Example: If the string is '12391:Axyzz' then left_string is '12391' and right_string is 'Axyzz'.
The output_string would be 'X:Y'.

input_list: ['Dz2A:fg12x','A12z3:xy9z1']
output_list: ['013:23','03:24']
For the first string in the input_list, the left_string is 'Dz2A' and the alphabets found at 0, 1 and 3 indices.
The right_string is 'fg12x' and the integer digits found at 2 and 3 indices. So the output_string is "013:23".
Similarly for the second string in the input_list, the output_string would be "03:24".
Hence the output_list will be ["013:23", "03:24"]

Assumptions:
The input_list would contain at least one element
Each string element of input_list would contain only one colon (":")
Note:No need to validate assumptions

Sample Input and Expected Output:
=================================================================================
| intput_list                                   |   output_list                 |
=================================================================================
| ['1234:abcd','abcd:1234']                     | ['X:Y', '0123:0123']          |
| ['hea23rt:att34ack','hea23rt:',':att34ack']   | ['01256:34',01256:Y','X:34']  |
| ['hea23rt:']                                  | ['01256:Y']                   |
=================================================================================
"""


def find_index(text1, text2):
    alpha_index = list()
    int_index = list()

    for i, char in enumerate(text1):
        if char.isalpha():
            alpha_index.append(i)

    for i, char in enumerate(text2):
        if char.isdigit():
            int_index.append(i)

    if not alpha_index:
        alpha_index.append('X')
    if not int_index:
        int_index.append('Y')

    alpha_index = ''.join(list(map(str, alpha_index)))
    int_index = ''.join(list(map(str, int_index)))

    return ':'.join([alpha_index, int_index])


def fun(input_list):
    output_list = []
    # Write your logic here
    for s in input_list:
        output_list.append(find_index(*s.split(':')))

    return output_list


input_list = ['A12z3:xy9z1', 'Dz2A:fg12x']
output_list = fun(input_list)
print(output_list)
