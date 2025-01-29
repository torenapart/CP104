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
from functions import file_top
# Constants

filename = "students.txt"
file_handle = open(filename, "r", encoding="utf-8")
output = file_top(file_handle, 5)
print(output)
file_handle.close()
