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
# Constants
ANNUAL_TAX = 18.50

# Ask for inputs
totalsales = float(input("Enter the total sales: "))
print()
print("Projected Tax Report")
print("--------------------------")
print(f"Total Sales:   ${totalsales}")
print(f"Annual tax:    %{ANNUAL_TAX:.2f}")
print("--------------------------")

# Calculate tax
tax = (totalsales/100)*18.50

# Print tax
print(f"Tax:           ${tax:>10.2f}")
