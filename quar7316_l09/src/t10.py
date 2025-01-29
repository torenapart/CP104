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
from functions import text_analyze
# Constants
txt = str(input("Input a text you want to be analyzed: "))
print()
uppr, lowr, dgts, whtspc = text_analyze(txt)
print(
    f"The amount of uppercase letters is: {uppr}, The amount of lowercase letters is: {lowr}, The amount of digits is: {dgts}, and the amount of whitespaces is: {whtspc}")
