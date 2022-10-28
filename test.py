import locale
from datetime import datetime, date, timedelta
import datetime as dt
import calendar

# locale.setlocale(locale.LC_ALL, 'de_DE')
date_today = datetime.now()
current_date = date.today()
current_month = calendar.monthcalendar(year = current_date.year, month = current_date.month)

def next_day():
    next_date = datetime.today() + dt.timedelta(days = 1)
    next_date_formatted = next_date.strftime("%A %d, %B %Y")
    return next_date_formatted

def last_day():
    largest_number = current_month[0][0]
    for entry in current_month:
        for x in entry:
            if x >  largest_number:
                largest_number = x
    return largest_number

def today_decimal():
    return int(date_today.strftime("%d"))

def month_first_day():
    first_day = date_today.replace(day=1)
    return first_day

def month_last_day():
    day_last = date_today.replace(day=last_day())
    return day_last

def month_day(day):
    return date_today.replace(day=day)

def km_month():
    total_km = 0
    for x in range(month_first_day().day, today_decimal() + 1):
        daily_km = int(input("How much did you ride on {}: ".format(month_day(x).strftime("%A %d, %B %Y"))))
        total_km = total_km + daily_km
    return ("You have driven this month: {} km".format(total_km))

print(km_month())