"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-09-23"
-------------------------------------------------------
"""
# Imports

# Ask for amount of time
Time = int(input("Enter number of minutes:"))
# Calculate Hours, Days, and Minutes
Hours = (Time//60) % 24
Days = (Time//60)//24
Minutes = (Time % 60)
# Print Output
print(
    f"There are {Days} days, {Hours} hours, and {Minutes} minutes in {Time} minutes")
