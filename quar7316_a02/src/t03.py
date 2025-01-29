"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Ask for date
date = int(input(("Enter a date in the format YYYYMMDD: ")))
print()

# Separate the digits
year = date//10000
calcmonth = year*10000
month = (date-calcmonth)/100
precalcday = date//100
calcday = precalcday*100
day = (date-calcday)

# Print the reformatted date
print(f"The reformatted date: {year:.0f}/{month:.0f}/{day:.0f}")
