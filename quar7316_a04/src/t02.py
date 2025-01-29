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
# Imports
from functions import pollution_ranking
# Constants

airqual = int(input("""Give the AQI that you want translated to a safety. 

    PS."Good" - 0 to 50 AQI
    "Moderate" - 51 - 100 AQI
    "Unhealthy for Sensitive Groups" - 101 - 150 AQI
    "Unhealthy" - 151 - 200 AQI
    "Very Unhealthy" - 201 - 300 AQI
    "Hazardous" - 300+ AQI 
    
    You can input the AQI here: """))

output = pollution_ranking(airqual)
print()
print(output)
