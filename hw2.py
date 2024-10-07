import random

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