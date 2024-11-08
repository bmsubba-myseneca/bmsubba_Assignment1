from datetime import date, timedelta

def after(date_str):
    """Returns the day after the given date (as a string)."""
    dt = date.fromisoformat(date_str)
    next_day = dt + timedelta(days=1)
    return next_day.isoformat()

def day_of_week(year, month, day):
    """Returns the day of the week for a given date as a lowercase string (e.g., 'mon', 'tue')."""
    dt = date(year, month, day)
    return dt.strftime('%a').lower()

def mon_max(month, year):
    """Returns the maximum days in the given month, considering leap years."""
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    return 31

def leap_year(year):
    """Determines if a given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

def valid_date(date_str):
    """Checks if the date string is a valid date."""
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

def latest_date(date_str1, date_str2):
    """Returns the latest of two date strings in ISO format."""
    dt1 = date.fromisoformat(date_str1)
    dt2 = date.fromisoformat(date_str2)
    return max(dt1, dt2).isoformat()

def day_count(start_date_str, end_date_str):
    """Returns the number of weekend days between two dates."""
    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)
    
    if start_date > end_date:
        return 0
    
    current_date = start_date
    weekends = 0

    while current_date <= end_date:
        if current_date.weekday() >= 5:  # 5: Saturday, 6: Sunday
            weekends += 1
        current_date += timedelta(days=1)

    return weekends
