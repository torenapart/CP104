"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports
from functions import calc_factorial

# Constants
num = int(input("Input a number to find the n! of: "))
product = calc_factorial(num)
print(product)
