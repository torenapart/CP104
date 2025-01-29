"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics
# Constants


filename = "addresses.txt"
file_handle = open(filename, "r", encoding="utf-8")
output = file_statistics(file_handle)
print(output)
file_handle.close()
