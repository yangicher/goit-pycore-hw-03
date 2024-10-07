import re

pattern = r'^(\+38|38)?0?(\d{9})$'

def normalize_phone(phone_number : str):
    phone_number = re.sub('[^\d\+]', '', phone_number)    
    match = re.match(pattern, phone_number)
    if match:
        prefix, number = match.groups()
        if not prefix:
            return f'+380{number}'
        elif prefix == '38':
            return f'+{prefix}0{number}'
        else: 
            return f'{prefix}0{number}'
    return None

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)