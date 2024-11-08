import sys
import os
import datetime
from datetime import timedelta, date

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
