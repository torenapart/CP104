"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports
from functions import get_month_name
# Constants
monthgiven = int(input(
    "This function will return the name of a month given a number (int 1 <= m <= 12): "))
print()
numba = get_month_name(monthgiven)
print(numba)
