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
cost = float(input("Cost of 1 dosa:"))
dosa = float(input("Number of dosa:"))

# Calculate
price = cost*dosa
print()
print(f"Total cost of {dosa} dosas: ${price:.2f}")
