"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import largest_average
# Constants

val1 = float(input("Input the first value here: "))
print()
val2 = float(input("Input the second value here: "))
print()
val3 = float(input("Input the third value here: "))
print()

avg = largest_average(val1, val2, val3)

print(avg)
