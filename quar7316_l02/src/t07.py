"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-12-03"
-------------------------------------------------------
"""
NUMOFFLYERS = int(input("Input the numbers of flyers here: "))
NUMOFVOL = int(input("Input number of volunteers here: "))

per = NUMOFFLYERS//NUMOFVOL
rem = NUMOFFLYERS % NUMOFVOL

print(f"Flyers per volunteer: {per}")
print(f"Flyers left over: {rem}")
