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
from functions import factor_summation

# Constants
number = int(
    input("Input the number you want to calculate the factor summation of: "))
print()
total = factor_summation(number)
print(total)
