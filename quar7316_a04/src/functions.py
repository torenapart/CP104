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


def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    if day_num == 1:
        output = "Sunday"

    if day_num == 2:
        output = "Monday"

    if day_num == 3:
        output = "Tuesday"

    if day_num == 4:
        output = "Wednesday"

    if day_num == 5:
        output = "Thursday"

    if day_num == 6:
        output = "Friday"

    if day_num == 7:
        output = "Saturday"

    elif day_num > 7 or day_num < 1:
        output = "Error"

    return output


def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """

    if air_quality_index >= 0 and air_quality_index <= 50:
        output = "Good"

    elif air_quality_index >= 51 and air_quality_index <= 100:
        output = "Moderate"

    elif air_quality_index >= 101 and air_quality_index <= 150:
        output = "Unhealthy for Sensitive Groups"

    elif air_quality_index >= 151 and air_quality_index <= 200:
        output = "Unhealthy"

    elif air_quality_index >= 201 and air_quality_index <= 300:
        output = "Very Unhealthy"

    elif air_quality_index >= 300:
        output = "Hazardous"

    else:
        output = "Error"

    return output


def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    if val1 >= val2 and val1 >= val3:
        larg1 = val1
        if val2 > val3:
            larg2 = val2
        else:
            larg2 = val3
    elif val2 >= val1 and val2 >= val3:
        larg1 = val2
        if val1 >= val3:
            larg2 = val1
        else:
            larg2 = val3
    else:
        larg1 = val3
        if val2 >= val1:
            larg2 = val2
        else:
            larg2 = val1
    average = (larg1+larg2)/2
    return average


def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if rgb_colour1 == "red":
        if rgb_colour2 == "blue":
            rgb_colour = "fuchsia"

        elif rgb_colour2 == "green":
            rgb_colour = "yellow"

        elif rgb_colour2 == "red":
            rgb_colour = "red"

        else:
            rgb_colour = "Error"

    elif rgb_colour1 == "blue":
        if rgb_colour2 == "red":
            rgb_colour = "fuchsia"

        elif rgb_colour2 == "green":
            rgb_colour = "aqua"

        elif rgb_colour2 == "blue":
            rgb_colour = "blue"

        else:
            rgb_colour = "Error"

    elif rgb_colour1 == "green":
        if rgb_colour2 == "red":
            rgb_colour = "yellow"

        elif rgb_colour2 == "blue":
            rgb_colour = "aqua"

        elif rgb_colour2 == "green":
            rgb_colour = "green"

        else:
            rgb_colour = "Error"
    else:
        rgb_colour = "Error"
    return rgb_colour


def hoo_rah(number):
    """
    -------------------------------------------------------
    Takes an integer parameter and determines if its divisible 
    by 2,7, both, or none
    Returns "Zip" if it is not divisible by 2,7, or both.
        "2": "Hoo"
        "7": "Rah"
        "14": "Hoo Rah"
        "3": "Zip"
    Use: num = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number - must be an integer (int)
    Returns:
        response - either: Hoo, Rah, Hoo Rah, or Zip depending
        on what its divisble by
    -------------------------------------------------------
    """
    rem2 = number % 2
    rem7 = number % 7

    if rem2 == 0:
        if rem7 == 0:
            response = "Hoo Rah"
        elif rem7 != 0:
            response = "Hoo"
    elif rem7 == 0:
        if rem2 == 0:
            response = "Hoo Rah"
        elif rem2 != 0:
            response = "Rah"
    elif rem2 == 0 and rem7 == 0:
        response = "Zip"

    else:
        response = "Zip"
    return response
