"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import day_name
# Constants
day = int(input("""Input a Number for the day of the week.

(PS. Day 1 is "Sunday", day 7 is "Saturday")

Input your number here: """))
output = day_name(day)
print()
print(output)
