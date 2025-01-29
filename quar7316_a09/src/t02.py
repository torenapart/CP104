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
from functions import read_integers
# Constants
filename = "students.txt"
file_handle = open(filename, "r", encoding="utf-8")
output = read_integers(file_handle)
print(output)
file_handle.close()
