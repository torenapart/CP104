"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-09-28"
-------------------------------------------------------
"""
# Constants
CONVERSION = 1.61

# Ask for Mile input
miles = float(input("Length in miles:"))

# Complete Math
km = miles*CONVERSION

# Print answer
print()
print(f"Length in km: {km:.0f}")
