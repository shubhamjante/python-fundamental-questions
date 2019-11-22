"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
Write a python program to find and display the number of circular primes less than the given limit.
"""


def check_prime(number):
    pass #remove pass and write your logic here. if the number is prime return true, else return false


def rotations(num):
    pass #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]


def get_circular_prime_count(limit):
    pass #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.


#Provide different values for limit and test your program
print(get_circular_prime_count(1000))