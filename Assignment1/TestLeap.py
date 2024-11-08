def leap_year(year: int) -> bool:
    # A year is a leap year if it is divisible by 4, except for years divisible by 100,
    # unless they are also divisible by 400.
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
