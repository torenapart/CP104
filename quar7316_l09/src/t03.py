"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import parse_code

# Constants
prodcode = str(input("Input a parses code here to get dissect the category part, the id, the qualifier: "))
print()
pc, pi, pq = parse_code(prodcode)
print(f"The category part is: {pc}, The ID part is: {pi}, The qualifier part is {pq}")
