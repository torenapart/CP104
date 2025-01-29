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
from functions import colour_combine
# Constants
rgb_colour1 = str(
    input("Input your first RGB colour  that you intend to mix: "))
print()
rgb_colour2 = str(
    input("Input your second RGB colour that you intend to mix into the first: "))
output = colour_combine(rgb_colour1, rgb_colour2)
print()
print(output)
