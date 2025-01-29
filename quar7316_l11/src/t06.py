"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats
# Constants

smallest, largest, total, average = matrix_stats(
    [[2, 0, -1, 1], [10, 4, -5, 9], [-6, 3, 6, 0]])
print(f"{smallest}, {largest}, {total}, {average}")
