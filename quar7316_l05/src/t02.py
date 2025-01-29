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
from functions import get_weight

# Ask for user input
mass = float(input("What is the mass of the object in newtons: "))
weight, message = get_weight(mass)
print()
print(message)
