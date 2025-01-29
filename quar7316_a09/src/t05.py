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
from functions import student_stats
# Constants

filename = "students.txt"
file_handle = open(filename, "r", encoding="utf-8")
l_id, h_id, avg = student_stats(file_handle)
print(f"ID of the lowest mark: {l_id}, ID of the highest: {h_id}, and the average: {avg}")
file_handle.close()
