"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports
from functions import list_factors

# Constants
number = int(input("Give a number that you want the factors of: "))
factors = list_factors(number)
print()
print(factors)
