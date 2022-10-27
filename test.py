import locale
from datetime import datetime, date
import datetime as dt
import calendar

# locale.setlocale(locale.LC_ALL, 'de_DE')
date_today = datetime.now()
current_date = date.today()
current_month = calendar.monthcalendar(year = current_date.year, month = current_date.month)

def next_date():
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
    date = date_today.replace(day=1).strftime("%A %d, %B %Y")
    return date

def month_last_day():    
    date = date_today.replace(day=last_day()).strftime("%A %d, %B %Y")
    return date

def km_month():
    for x in range(1,today_decimal() +1):
        daily_km = int(input("How much did you ride on {}: ".format(month_first_day())))
    return daily_km

print(km_month())
