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
from functions import customer_best
# Constants
filename = "customers.txt"
fh = open(filename, "r", encoding="utf-8")
result = customer_best(fh)
fh.close
print(result)
