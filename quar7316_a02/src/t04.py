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
NUM_OF_FLYERS = int(input("Number of flyers:"))
NUM_OF_DELIV = int(input("Number of delivery people:"))

# Calculate Distributions
flyersper = NUM_OF_FLYERS//NUM_OF_DELIV
remainder = NUM_OF_FLYERS % flyersper
print()
# Print divided flyers and remainder
print(f"Flyers per delivery person: {flyersper}")
print(f"Flyers left over: {remainder}")
