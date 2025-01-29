"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports

# Constants


def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced = ""
    for s in sentence:
        if s.isupper() and spaced:
            spaced += " "
        spaced += s
    oldspaced = spaced
    oldspaced = oldspaced[1:]
    oldspaced = oldspaced.lower()
    spaced = spaced[:1]
    spaced = spaced + oldspaced
    return spaced


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    PRLOY = "oy"
    PRLAY = "ay"
    PRLES = "es"
    PRLS = "s"
    PRLSH = "sh"
    PRLCH = "ch"
    PRLY = "y"
    PRLIES = "ies"
    lngth = len(string)
    if string.endswith(PRLS):
        pluralized = string + PRLES
    elif string.endswith(PRLSH):
        pluralized = string + PRLES
    elif string.endswith(PRLCH):
        pluralized = string + PRLES
    elif string.endswith(PRLY):
        removal = string[lngth-2:lngth]
        if removal == PRLOY or removal == PRLAY:
            pluralized = string + PRLS
        else:
            prestring = string[:lngth-1]
            pluralized = prestring + PRLIES
    else:
        pluralized = string + PRLS

    return pluralized


def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    suffix = ''
    i = 1
    j = 1
    lngth = len(str1)
    lngth2 = len(str2)
    while i <= lngth and j <= lngth2 and str1[-i] == str2[-j]:
        suffix = str1[-i] + suffix
        i += 1
        j += 1

    return suffix


def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes 
        - its first group of digits is either '978' or '979' 
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    dash1 = isbn[3:4]
    dash2 = isbn[5:6]
    dash3 = isbn[8:9]
    dash4 = isbn[15:16]
    first3 = isbn[:3]
    last1 = isbn[16:]
    #last2check = isbn[15:]
    is_valid = False
    length = len(isbn)
    if length == 17:
        for s in isbn:
            if (s.isdigit() or s == '-'):
                if dash1 == "-" and dash2 == "-" and dash3 == "-" and dash4 == "-":
                    if first3 == "978" or first3 == "979":
                        if last1.isdigit():
                            is_valid = True
    return is_valid


def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = True
    length = len(words)
    s = 1

    while s < length:
        if words[s - 1][-1] != words[s][0]:
            word_chain = False
        s += 1

    return word_chain
