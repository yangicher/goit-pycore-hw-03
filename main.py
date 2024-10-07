from datetime import datetime
import random

def get_days_from_today(date : str) -> int:
    'string, format -> new datetime parsed from a string ("YYYY-MM-DD").'
    try: 
        res = (datetime.now() - datetime.strptime(date, "%Y-%m-%d"))
        return res.days
    except ValueError as e: 
        print('ValueError Raised:', e) 

def get_numbers_ticket(min : int, max : int, quantity : int):
    """min -> positive number, 
       max -> less than 1000 or equal,
       quantity -> result amount"""
    if(min < 1 or max > 1000):
        return []
    elif(max + 1 - min >= quantity):
        numbers = [i for i in range(min, max + 1)]
        chosen_numbers = random.sample(numbers, quantity)
        return sorted(chosen_numbers)
    return []

print(get_days_from_today("2025-10-05"))
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)