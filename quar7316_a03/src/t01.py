"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import footage_to_acres

foot = float(input("Input your feet that you want converted: "))
output = footage_to_acres(foot)
print()
print(output)
