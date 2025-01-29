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
from functions import lawn_mow_time

# Ask for inputs
width = float(input("Input your width here: "))
print()
length = float(input("Input your length here: "))
print()
speed = float(input("Input your speed here: "))

# Call the function
estimatedtime = lawn_mow_time(width, length, speed)

# Print outcome
print()
print(f"{estimatedtime:.1f}")
