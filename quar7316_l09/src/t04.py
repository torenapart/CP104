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
from functions import validate_code
# Constants
product_code = str(input("Input a product code here to see the category, digits, and qualifiers: "))
print()
category, digits, qualifiers = validate_code(product_code)
print(f"The category is: {category}, The digits are: {digits}, and the qualifiers are: {qualifiers}")
