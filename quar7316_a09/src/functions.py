"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports

# Constants


def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line_number = 0
    line = file_handle.readline()

    while line and line_number < count:
        print(line, end="")
        line_number += 1
        line = file_handle.readline()

    return


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    line = file_handle.readline()

    while line != "":
        tokens = line.strip().split(',')
        i = 0
        while i < len(tokens):
            if tokens[i].isdigit():
                num = int(tokens[i])
                if num > 0:
                    number_list.append(num)
            i += 1
        line = file_handle.readline()
    return number_list


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    lines = file_handle.read()
    i = 0
    while i < len(lines):
        spot = lines[i]
        if spot.isupper():
            ucount += 1
        elif spot.islower():
            lcount += 1
        elif spot.isdigit():
            dcount += 1
        elif spot.isspace():
            wcount += 1
        else:
            rcount += 1
        i += 1

    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line_number = 0
    line = fh_read.readline()

    while line:
        formatted_line = f"[{line_number}] {line}"
        fh_write.write(formatted_line)
        line_number += 1
        line = fh_read.readline()

    return


def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    total_marks = 0
    count = 0
    lowest_mark = float('inf')
    highest_mark = float('-inf')
    l_id = "lowest_id"
    h_id = "highest_id"
    line = file_handle.readline()

    while line:
        tokens = line.strip().split(',')

        if len(tokens) == 4:
            student_id = tokens[2]
            mark = float(tokens[3])
            total_marks += mark
            count += 1

            if mark < lowest_mark:
                lowest_mark = mark
                l_id = student_id

            if mark > highest_mark:
                highest_mark = mark
                h_id = student_id

        line = file_handle.readline()
    avg = total_marks / count

    return l_id, h_id, avg
