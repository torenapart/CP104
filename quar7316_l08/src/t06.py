"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""
# Imports
from functions import list_stats
# Constants

smallest, largest, total, average = list_stats(
    [94, 96, -22, -79, -28, -26, -50, 71, 24, -32])
print(
    f"Smallest: {smallest} large:{largest}, total: {total}, average: {average}")
