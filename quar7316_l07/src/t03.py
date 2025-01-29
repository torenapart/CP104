"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from functions import population_growth
# Constants
target = int(input("Input the target population number: "))
print()
current = int(input("Input the current population number: "))
print()
rate = int(input("Input the rate at which the population grows: "))
print()
years = population_growth(target, current, rate)
print(f"It will take {years} years to reach the population of {target}")
