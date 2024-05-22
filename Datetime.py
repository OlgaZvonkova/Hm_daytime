from datetime import datetime

d = input("Enter year, month, day separated by hyphen (-): ")
year, month, day = map(int, d.split('-'))

def get_days_from_today(date_str):
    d = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.today()
    delta = today - d
    return delta.days

delta = get_days_from_today(d)
print("Days from today:", delta)
 