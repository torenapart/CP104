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
from functions import employee_payroll
# Constants


total, average = employee_payroll()
print()
print(f"The total is: {total:,.2f}, and the average is: {average:,.2f}")
