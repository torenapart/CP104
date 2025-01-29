"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from functions import get_int
# Constants
low = int(input("Give a number that the value must be greater than: "))
print()
high = int(input("Give a number that the value must be lesser than: "))
print()
value = get_int(low, high)
print(value)
