"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports

# Constants
from functions import multiplication_table
start = int(input("Input the number to start the multiplication table with: "))
print()
end = int(input("Input the number to end the multiplication table with: "))
print()
multiplication_table(start, end)
