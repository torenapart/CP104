"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports

# Constants


def list_factors(number):
    """
    -------------------------------------------------------
    Takes an int greater than 0 and returns a list of factors
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 0)
    Returns:
        factors - a list of factors (str)
    -------------------------------------------------------
    """
    factors = []
    for i in range(1, number, 1):
        rem = number % i
        if rem == 0:
            factors += [i]

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []
    number = int(input("Enter a positive number: "))
    while number != 0:
        if number > 0:
            number_list += [number]
        number = int(input("Enter a positive number: "))

    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []
    i = 0
    n = len(numbers)
    while i < n:
        equal = numbers[i]
        if equal == target_number:
            index_list += [i]
        i += 1

    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    temp = []

    for v in minuend:
        if v not in subtrahend:
            temp.append(v)
    minuend[:] = []

    for v in temp:
        minuend.append(v)

    return


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1

    n = len(numbers)
    i = 0

    while i < n - 1 and in_order:
        current = numbers[i]
        next_value = numbers[i + 1]

        if current > next_value:
            in_order = False
            index = i

        i += 1

    return in_order, index
