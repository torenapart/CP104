"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from random import randint, randrange, random, uniform
# Constants


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    if value_type == "int":
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(randint(low, high))
            matrix.append(row)
    elif value_type == "float":
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(uniform(low, high))
            matrix.append(row)
    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    if value_type == 'float':
        formatter = '.2f'
        print("   ", end="")

        for j in range(len(matrix[0])):
            print(f"{j:^8}", end="")

            print()

        for i in range(len(matrix)):
            print(f"{i:<3}", end="")

        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:^8.{formatter}}", end="")

        print()
    else:
        formatter = 'd'
        print("   ", end="")

        for j in range(len(matrix[0])):
            print(f"{j:^8}", end="")

            print()

        for i in range(len(matrix)):
            print(f"{i:<3}", end="")

        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:^8.{formatter}}", end="")

        print()

# i didnt make this just so this code under it can work


def generate_matrix_char(rows, cols):
    """
    Generates a 2D list of random lower case letter ('a' - 'z') values

    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)

    Returns:
        matrix - a 2D list of random characters (2D list of str)
    """
    # Check if rows and cols are valid
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be greater than 0")

    # Generate a matrix with random lowercase letters
    matrix = [[random.choice('abcdefghijklmnopqrstuvwxyz')
               for _ in range(cols)] for _ in range(rows)]

    return matrix


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    for i in range(0, len(matrix[0])):

        print(f"{i:5d} |", end="")

        for char in range(matrix[0][i], matrix[2][i]):

            print(f"{char:5d}", end="")

        print()


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    total = 0
    smallest = 0
    largest = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = matrix[i][j]
            total += current
            if current > largest:
                largest = current
            elif current < smallest:
                smallest = current
    numbers = len(matrix) + len(matrix[i])
    average = total/numbers

    return smallest, largest, total, average


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    max = 0
    min = 0
    s_loc = [0, 0]
    l_loc = [0, 0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = matrix[i][j]
            if current > max:
                max = current
                l_loc = [i, j]
            elif current < min:
                min = current
                s_loc = [i, j]

    return s_loc, l_loc
