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
# Ask for inputs
number = int(input("Enter a positive digit number: "))

# Separate digits
firstnumber = number//10
secondnumber = number % 10

# Find the difference
output = firstnumber-secondnumber
print()
# Print the difference
print(f"The difference of the digits of {number} is {output}")
