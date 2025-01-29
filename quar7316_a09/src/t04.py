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
from functions import line_numbering
# Constants


filename = "wilde.txt"
fh_read = open(filename, "r", encoding="utf-8")
fh_write = open("wilde_numbered.txt", "w", encoding="utf-8")
line_numbering(fh_read, fh_write)
fh_read.close()
fh_write.close()
