from datetime import datetime, timedelta

upcoming_period = 7
days_in_week = 7

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    for user in users:
        today = datetime.now()

        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        birthday_this_year = user_birthday.date().replace(year=today.year)
        
        if (birthday_this_year < today.date()):
            birthday_this_year = user_birthday.date().replace(year=today.year + 1)

        diff = (birthday_this_year - today.date()).days

        if(diff >= 0 and diff <= upcoming_period): 
            weekday = birthday_this_year.weekday()
            if(weekday == 6 or weekday == 5):
                begin_week = birthday_this_year + timedelta(days = days_in_week - weekday)
                upcoming_birthdays.append(f"name: {user["name"]}, congratulation_date: {begin_week.strftime("%Y.%m.%d")}")
            else:
                upcoming_birthdays.append(f"name: {user["name"]}, congratulation_date: {birthday_this_year.strftime("%Y.%m.%d")}")
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.08"},
    {"name": "Jane Smith", "birthday": "1990.03.14"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)