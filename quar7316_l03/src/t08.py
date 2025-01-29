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

# Ask for float inputs
dirt = float(input("Enter amount of dirt (m^3):"))
gravel = float(input("Enter amount of gravel (m^3):"))
sand = float(input("Enter amount of sand (m^3):"))
# Calculate Total
Total = dirt+gravel+sand
print()
# Print Output
print("Material   Cubic Metres")
print(f"Dirt       {dirt:5.1f}")
print(f"Gravel     {gravel:5.1f}")
print(f"Sand       {sand:5.1f}")
print(f"Total      {Total:5.1f}")
