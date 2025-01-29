"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
from functions import hoo_rah

number = int(input("""Insert number here to see what its divisible by 

PS: "Hoo" for 2, "Rah" for 7, "Hoo Rah" for 2 and 7, and "Zip" for none.

Insert your number here: """))

response = hoo_rah(number)
print()
print(response)
