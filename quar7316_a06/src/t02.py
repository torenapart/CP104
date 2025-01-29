"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import detect_prime
# Constants
number = int(input("Input a number to see if it's a prime number or not: "))
print()
boolean = detect_prime(number)
print(boolean)
