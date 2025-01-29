"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports
from functions import calories_treadmill
# Constants
per_min = float(input("Input the Calories Burnt per minute: "))
minutes = int(input("Input the minutes worked out: "))

calories_treadmill(per_min, minutes)
