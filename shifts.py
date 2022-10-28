import locale
from datetime import datetime as dt, date
import calendar as cal

locale.setlocale(locale.LC_ALL, 'de_DE')
date_today = dt.now()
current_date = date.today()
current_month = cal.monthcalendar(year = current_date.year, month = current_date.month)

def last_day():
    largest_number = current_month[0][0]
    for entry in current_month:
        for x in entry:
            if x >  largest_number:
                largest_number = x
    return largest_number

def month_first_day ():
    date = date_today.replace(day=1).strftime("%A %d, %B %Y")
    return date

def month_last_day ():    
    date = date_today.replace(day=last_day()).strftime("%A %d, %B %Y")
    return date

print(month_last_day())