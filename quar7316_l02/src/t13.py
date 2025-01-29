"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports

# Constants
MIDTERM_WEIGHT = 0.35
FINAL_WEIGHT = 0.65
# Ask for user inputs
midterm = float(input("Midterm mark (%):"))
final = float(input("Exam mark (%):"))
# Calculate final mark
midterm_pre = MIDTERM_WEIGHT*midterm
final_pre = FINAL_WEIGHT*final
finalmark = final_pre+midterm_pre
print(finalmark)
