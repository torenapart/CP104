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
from functions import multiply_fractions

# Ask for inputs
n1 = int(input("Input Numerator 1 here: "))
d1 = int(input("Input Denominator 1 here: "))
n2 = int(input("Input Numerator 2 here: "))
d2 = int(input("Input Denominator 2 here: "))

# Recall Function
output = multiply_fractions(n1, d1, n2, d2)

# Print output
print(output)
