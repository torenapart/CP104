"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import customer_by_id
# Constants


filename = "customers.txt"
fh = open(filename, "r", encoding="utf-8")
customer_ids = customer_by_id(fh, "12345")

print(customer_ids)
