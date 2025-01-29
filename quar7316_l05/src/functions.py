"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-12-04"
-------------------------------------------------------
"""
# Imports
from math import fabs


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    check = day*month
    if check == year:
        magic = True
    else:
        magic = False

    return magic


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    # Constants
    GRAVITY = 9.8

    # Ask for and Calculate User Inputs
    weight = mass*GRAVITY

    if weight > 1000:
        message = "heavy"

    elif weight < 10:
        message = "light"

    else:
        message = "average"

    return weight, message


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    # Find the difference distances
    onedist = fabs(target-v1)
    twodist = fabs(target-v2)

    # If statements to compare
    if onedist <= twodist:
        result = v1
    else:
        result = v2
    return result


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """

    if speed > 117:
        output = "Hurricane"

    elif speed >= 89:
        output = "Whole Gale"

    elif speed >= 62:
        output = "Gale Winds"

    elif speed >= 39:
        output = "Strong Wind"

    elif speed >= 0:
        output = "Breeze"

    else:
        output = "Unknown"
    return output


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Parameters: 
        years - years worked (int >= 5)
        salary - salary earnings (int >= 30,000)
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # Constants
    YEARREQ = 5
    WAGEREQ = 30000
    qualified = False

    # Ask for years employed
    years = int(input("Years Employed: "))

    # If eligible ask for salary
    if years >= YEARREQ:
        salary = int(input("Annual Salary: "))
        if salary >= WAGEREQ:
            qualified = True

    return qualified


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    # Constants
    cost = 0
    BURGER = 6.00
    WINGS = 8.00
    FRIES = 1.50
    SALAD = 2.00

    # Ask for order and such
    order = input("Order B - burger or W - wings: ")
    if order == "B":
        cost = cost + BURGER
    elif order == "W":
        cost = cost + WINGS
    combo = input("Make it a combo? (Y/N): ")
    if combo == "Y":
        choice = input("Add F - fries or S - salad: ")
        if choice == "F":
            cost = cost + FRIES
        elif choice == "S":
            cost = cost + SALAD
    elif combo == "N":
        cost = cost + 0
    print()
    print(f"{cost:.2f}")
    return cost
