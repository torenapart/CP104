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
MONTHINYEAR = 12
p = int(input("Input the initial mortgage principal amount: "))
years = int(input("Input the amount of years "))
interest = float(input("Yearly interest rate (%): "))
print()
n = years/MONTHINYEAR
i = interest/MONTHINYEAR

outputtop = p*(i*((1+i)**n))
outputbot = ((1+i)**n)-1
output = outputtop/outputbot
print(output)
