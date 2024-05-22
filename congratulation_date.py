from datetime import datetime, date, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]


def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    users = {"name":"birthday"}
    birthday_str = users.get("birthday")
    formatted_birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()
    today = datetime.today().date()
    for user in users:
        birthday_this_year= datetime(today.year, today.month, today.day).date 
        if birthday_this_year < today:
            next_year_birthday = formatted_birthday - timedelta(days=7)
        else:
            next_birth= (formatted_birthday - today).strptime("%A, %d %B %Y")
        return  upcoming_birthdays
res= get_upcoming_birthdays(users)
print (res)           
