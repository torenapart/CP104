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
LARGEP = 75.00
SMALLP = 50.00

largenum = int(input("How many large dogs did you groom today?: "))
smallnum = int(input("How many small dogs did you groom today?: "))

largeprice = LARGEP * largenum
smallprice = smallnum * SMALLP

finalprice = largeprice + smallprice

print()
print(f"Your final price is ${finalprice:.2f}")
