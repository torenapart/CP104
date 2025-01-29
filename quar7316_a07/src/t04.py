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
from functions import list_subtract, list_positives
# Constants

subnum = int(input("Enter a number to remove from the minuend: "))
print()
subtrahend = [subnum]
minuend = list_positives()
print()
print(f"Old Minuend: {minuend}")
print()
list_subtract(minuend, subtrahend)
print(f"New Minuend: {minuend}")
