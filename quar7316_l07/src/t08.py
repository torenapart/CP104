"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from functions import budget
available = float(input("What is your available amount of money? $"))
expenses, balance, status = budget(available)
print(
    f"Total Expenses: {expenses}, New Balance: {balance}, Status: {status}")
