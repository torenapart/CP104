"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import interest_table
# Constants
principal = float(input("Input the Principal payment here: "))
print()
interest = float(input("Input the yearly interest here: "))
print()
payment = float(input("Input the payments here: "))
print()
interest_table(principal, interest, payment)
