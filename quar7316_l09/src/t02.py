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
from functions import url_categorize
# Constants
url = str(input("Input a url to catergorize what type of url it is: "))
print()
urltype = url_categorize(url)
print(urltype)
