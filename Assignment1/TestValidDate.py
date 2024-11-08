from datetime import datetime

def valid_date(date_str: str) -> bool:
    try:
        # Attempt to parse the date string in the format YYYY-MM-DD
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        # If parsing fails, the date is invalid
        return False
