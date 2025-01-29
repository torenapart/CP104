"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Greet user and ask for Celsius temperature
celsius = int(input("Hello, enter your celsius temperature here:"))

# Water freezes @ 32 degrees
FREEZING_TEMP = 32

# State the Fahrenheit formula
fahrenheit = int(((9/5)*celsius + 32))
print(int(fahrenheit))
