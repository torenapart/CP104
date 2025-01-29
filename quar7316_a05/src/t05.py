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
from functions import range_addition
start = int(input("Input the starting number here: "))
print()
end = int(input("Input the ending number here: "))
print()
increment = int(input("Input the increment here: "))
print()
total = range_addition(start, end, increment)
print(total)
