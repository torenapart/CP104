"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-09-28"
-------------------------------------------------------
"""

# Ask for user inputs
principal = float(input("Principal:"))
interest = float(input("Interest (%):"))
years = int(input("Number of years:"))
compound = int(input("Number of times interest compounded per year:"))

interestpercent = interest/100
# Calculate the output
output = (principal*((1+(interestpercent/compound))**(compound*years)))
print(f"Balance:${output:.2f}")
