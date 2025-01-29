"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""
# Imports
from random import randint, randrange, random, uniform
# Constants


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    count = 0
    number = randint(1, high)
    guess = int(input("Guess:"))
    print()
    while guess != number:
        if guess > number:
            print("Too high, try again")
            print()
            count += 1

        elif guess < number:
            print("Too low, try again")
            print()
            count += 1

        guess = int(input("Guess:"))
        print()

    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 0
    number = 0
    while target > number:
        number = 2**power
        power += 1
    return number


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    ratefloat = rate/100

    while current < target:
        current += current*ratefloat
        years += 1

    return years


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    inputs = 0
    total = 0
    value = float(input("First positive value: "))
    minimum = value
    maximum = value
    while value >= 0:
        total += value
        inputs += 1
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
        value = float(input("Next positive value: "))
    average = total/inputs
    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    expenses = 0
    expense = float(input("Enter an expense (0 to quit): $"))
    while expense > 0:
        expenses += expense
        expense = float(input("Enter another expense (0 to quit): $"))
    balance = available - expenses
    if balance > 0:
        status = "Surplus"
    elif balance < 0:
        status = "Deficit"
    else:
        status = "Balanced"
    return expenses, balance, status


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the highest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f"Enter a value between {low} and {high}: "))

    while value > high or value < low:
        if value < low:
            print("Value entered is too low")
        elif value > high:
            print("Value entered is too high")
        value = int(input(f"Enter a value between {low}  and {high}: "))
    return value


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    hours = 0
    total = 0
    inputs = 0
    TAXRATE = 0.03625
    empnumber = int(input("Employee ID: "))
    while empnumber > 0:
        inputs += 1
        hourate = float(input("Hourly wage rate: "))
        hours = float(input("Hours worked: "))
        print()

        if hours > 40:
            OVERTIME = hours-40
            OVERTIMERATE = OVERTIME*(hourate*1.5)
            gross = (40*hourate) + OVERTIMERATE

        else:
            gross = hourate*hours

        tax = gross*TAXRATE
        net = gross - tax
        total += net
        empnumber = int(input("Employee ID: "))
    average = total/inputs

    return total, average
