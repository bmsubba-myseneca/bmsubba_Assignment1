def mon_max(month: int, year: int) -> int:
    # Check if year is a leap year
    def is_leap_year(y: int) -> bool:
        if y % 4 == 0:
            if y % 100 == 0:
                return y % 400 == 0
            return True
        return False
    
    # Dictionary of days in each month for a common year
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Adjust February for leap years
    if month == 2 and is_leap_year(year):
        return 29
    
    return days_in_month.get(month, 0)  # Return days in the specified month
