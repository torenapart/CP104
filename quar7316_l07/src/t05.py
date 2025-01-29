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
from functions import positive_statistics

minimum, maximum, total, average = positive_statistics()
print(
    f"Minimum : {minimum:.2f} Maximum: {maximum:.2f} Total: {total:.2f} Average: {average:.2f}")
