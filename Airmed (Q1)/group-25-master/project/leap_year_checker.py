def is_leap_year(year):
    """Returns True iff. the given year is a leap year.

    :param year: the year to be checked
    :return: Whether the given year is a leap year
    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            return (year % 400) == 0
        else:
            return True
    else:
        return False
