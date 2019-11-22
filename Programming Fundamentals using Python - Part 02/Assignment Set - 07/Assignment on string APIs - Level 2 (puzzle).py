"""
Write a python program to validate the details provided by a user as part of registering to a web application.

Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets

Write a function validate_phone_no(phoneno) to validate the phone number
    Phone number should have 10 digits
    Phone number should not have any characters or special characters
    All the digits of the phone number should not be same.
    Example: 9999999999 is not a valid phone number

Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com

All the functions should return true if the corresponding value is valid. Otherwise, it should return false.

Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the
arguments passed to it and display appropriate message. Refer the comments provided in the code.

Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.
"""


def validate_name(name):
    if name == '' or len(name) > 15 or not name.isalpha():
        return False
    else:
        return True


def validate_phone_no(phno):
    if len(phno) != 10 or not phno.isdigit() or not len(set(phno)) != 1:
        return False
    else:
        return True


def validate_email_id(email_id):
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com']

    if email_id.count('@') != 1 or email_id.count('.com') != 1 or not email_id.endswith('.com') or\
            email_id.split('@')[-1] not in domains:
        return False
    else:
        return True


def validate_all(name,phone_no,email_id):
    if not validate_name(name):
        print("Invalid Name")
    elif not validate_phone_no(phone_no):
        print("Invalid phone number")
    elif not validate_email_id(email_id):
        print("Invalid email id")
    else:
        print("All the details are valid")


validate_all("Tina", "9994599998", "tina@yahoo.com")