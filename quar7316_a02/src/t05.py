"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Ask User for inputs
length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
height = float(input("Foundation height (m): "))
wallheight = float(input("Wall height (m): "))
costconcrete = float(input("Cost of concrete ($/m^3): "))
costbricks = float(input("Cost of bricks ($/m^2): "))

# Calculate volume and wall area
foundationvol = length*width*height
wallvol = ((length*2)+(width*2))*wallheight

# Calculate Prices
priceconcrete = foundationvol*costconcrete
pricebrick = wallvol*costbricks
finalprice = priceconcrete+pricebrick

# Print Prices
print()
print(f"Concrete needed for foundation (m^3): {foundationvol:.2f}")
print(f"Cost of concrete: ${priceconcrete:,.2f}")
print(f"Bricks needed for walls (m^2): {wallvol:.2f}")
print(f"Cost of bricks: ${pricebrick:,.2f}")
print(f"Total cost: ${finalprice:,.2f}")
