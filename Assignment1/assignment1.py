import sys
import os
from datetime import date, timedelta

def after(input_date: str) -> str:
    """Return the date one day after the given date string."""
    try:
        date_obj = date.fromisoformat(input_date)
        next_day = date_obj + timedelta(days=1)
        return next_day.isoformat()
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def day_of_week(year: int, month: int, day: int) -> str:
    """Return the day of the week for a given date."""
    try:
        dobj = date(year, month, day)
        return dobj.strftime('%a').lower()
    except ValueError:
        raise ValueError("Invalid date parameters.")

def mon_max(month: int, year: int) -> int:
    """Return the maximum number of days in the given month of the given year."""
    if month == 1: return 31
    if month == 2: return 29 if leap_year(year) else 28
    if month == 3: return 31
    if month == 4: return 30
    if month == 5: return 31
    if month == 6: return 30
    if month == 7: return 31
    if month == 8: return 31
    if month == 9: return 30
    if month == 10: return 31
    if month == 11: return 30
    if month == 12: return 31
    raise ValueError("Invalid month")

def leap_year(year: int) -> bool:
    """Return True if the given year is a leap year, False otherwise."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def valid_date(date_str: str) -> bool:
    """Check if the given date string is a valid date in YYYY-MM-DD format."""
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

def latest_date(date1: str, date2: str) -> str:
    """Return the later of two dates."""
    dobj1 = date.fromisoformat(date1)
    dobj2 = date.fromisoformat(date2)
    return max(dobj1, dobj2).isoformat()

def day_count(start: str, end: str) -> int:
    """Return the number of weekends (Saturdays and Sundays) between two dates."""
    start_date = date.fromisoformat(start)
    end_date = date.fromisoformat(end)
    delta = end_date - start_date
    weekends = 0
    for i in range(delta.days + 1):
        current_day = start_date + timedelta(days=i)
        if current_day.weekday() >= 5:  # Saturday (5) or Sunday (6)
            weekends += 1
    return weekends

def usage():
    print("Usage: python assignment1.py <start_date> <end_date>")
    sys.exit(1)  # Exit after printing the usage message

def is_valid_date(date_str):
    try:
        date.fromisoformat(date_str)  # This will raise ValueError if the date is invalid
        return True
    except ValueError:
        return False

def count_work_days(start_date, end_date):
    WEEKDAY_FRIDAY = 4
    
    # Adjust start_date if it's past the week
    if start_date.weekday() > WEEKDAY_FRIDAY:
        start_date = start_date + timedelta(days=7 - start_date.weekday())

    # Adjust end_date if it's a weekend
    if end_date.weekday() > WEEKDAY_FRIDAY:
        end_date = end_date - timedelta(days=end_date.weekday() - WEEKDAY_FRIDAY)

    if start_date > end_date:
        return 0  # If start_date is after end_date, return 0 workdays
    
    # Total difference in days, including the end date
    diff_days = (end_date - start_date).days + 1
    weeks = diff_days // 7
    remainder = end_date.weekday() - start_date.weekday() + 1

    if remainder != 0 and end_date.weekday() < start_date.weekday():
        remainder = 5 + remainder

    return weeks * 5 + remainder

def main():
    # Check if the number of arguments is not 2
    if len(sys.argv) != 3:
        usage()  # Call usage if the number of arguments is incorrect

    start_date_str = sys.argv[1]
    end_date_str = sys.argv[2]

    # Check if the dates are valid
    if not (is_valid_date(start_date_str) and is_valid_date(end_date_str)):
        usage()

    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)

    # Sort dates if needed
    start, end = sorted([start_date, end_date])

    # Calculate the weekends
    delta = end - start + timedelta(days=1)  # Include end date in the count
    workdays = count_work_days(start, end)
    weekends = delta.days - workdays

    # Output the result
    print(f'The period between {start} and {end} includes {weekends} weekend days.')

if __name__ == '__main__':
    main()
