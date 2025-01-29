"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports

# Constants


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number+1, 1):
        product *= i
    return product


def calories_treadmill(per_min, minutes):
    """
    ------------------------------------------------------- 
    Prints a table of the number of calories burned every five minutes 
    given the number of calories burned per minute an the total number of minutes run.
    Use: burned = calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burnt per min (float > 0)
        minutes - minutes ran (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(5, minutes+5, 5):
        burnedpermin = per_min*i
        print(f"{i:>3d}  {burnedpermin:.1f}")

    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an arrow pointing up based on an integer parameter
    Use: rows = arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, rows+1, 1):
        side = " " * (rows - i)
        if i == 1:
            print(f"{side} #")
        else:
            middle = " " * (2 * (i - 2))
            print(f"{side} # {middle}#")
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(start_num, stop_num + 1):
        product = i*start_num
        for f in range(start_num, stop_num):
            product = i * f
            print(f"{product}")

    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    current = start
    for i in range(count):
        total += current
        current += increment
    return total
