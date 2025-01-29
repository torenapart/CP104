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
from functions import extract_date

# Ask for input
unfiltereddate = int(input("Input your unfiltered date here (YYYYMMDD): "))

# Recall function
year, month, day = extract_date(unfiltereddate)

# Print function
print()
print(f"{year}, {month}, {day}")
