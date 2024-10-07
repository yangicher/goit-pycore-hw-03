from datetime import datetime

def get_days_from_today(date : str) -> int:
    'string, format -> new datetime parsed from a string ("YYYY-MM-DD").'
    try: 
        res = (datetime.now() - datetime.strptime(date, "%Y-%m-%d"))
        return res.days
    except ValueError as e: 
        print('ValueError Raised:', e) 