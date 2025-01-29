"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports


def total_wins():
    """
    -------------------------------------------------------
    Returns the amount of times Purple or Gold team won
    Use: total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        purpwin - Number of Purple team wins (int)
        golwin - Number of Gold team wins (int)
    ------------------------------------------------------
    """
    purpwin = 0
    golwin = 0
    purp = "purple"
    gol = "gold"
    team = str(input("Enter the winning team: "))
    while team != "":
        if team == purp:
            purpwin += 1
        elif team == gol:
            golwin += 1
        team = str(input("Enter the winning team: "))
    return purpwin, golwin


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    i = 5
    if number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6

        return True


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    month = 1
    MONTHINTEREST = (interest_rate / 100) / 12
    remamt = principal_amount
    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")
    while remamt > 0:
        monthly_interest = remamt * MONTHINTEREST
        if remamt < payment:
            principal_amount = remamt
            payment = remamt + monthly_interest
        else:
            principal_amount = payment - monthly_interest
        remamt -= principal_amount
        print(f"{month:4} {monthly_interest:8.2f} {payment:8.2f} {remamt:8.2f}")
        month += 1
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 1
    if number < 0:
        absnumber = number+(number*-2)
        div = absnumber/10
        while div > 1:
            div /= 10
            digits += 1
    else:
        div = number/10
        while div > 1:
            div = div/10
            digits += 1
    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    i = 1
    while i < number:
        if number % i == 0:
            total += i
        i += 1
    return total
