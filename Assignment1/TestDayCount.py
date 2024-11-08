from datetime import datetime, timedelta

def day_count(start_date: str, end_date: str) -> int:
    # Convert the input strings to date objects
    start = datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.strptime(end_date, '%Y-%m-%d').date()
    
    # Ensure start is before end
    if start > end:
        start, end = end, start

    # Calculate total days in the date range
    total_days = (end - start).days + 1  # inclusive of both start and end
    
    # Count the number of weekdays (Monday-Friday)
    weekday_count = 0
    current = start
    while current <= end:
        if current.weekday() < 5:  # Monday to Friday (0 to 4)
            weekday_count += 1
        current += timedelta(days=1)

    # Calculate weekend days by subtracting weekdays from total days
    weekend_count = total_days - weekday_count
    return weekend_count
