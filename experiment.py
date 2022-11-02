import locale
from datetime import datetime as dt, date
import calendar as cal

# locale.setlocale(locale.LC_ALL, 'de_DE')
date_today = dt.now()
current_date = date.today()
current_month_array = cal.monthcalendar(year = current_date.year, month = current_date.month)
days = [] 

def last_day():
    largest_number = current_month_array[0][0]
    for entry in current_month_array:
        for x in entry:
            if x >  largest_number:
                largest_number = x
    return largest_number

def today_decimal():
    return int(date_today.strftime("%d"))

def month_first_day ():
    date = date_today.replace(day=1)
    return date

def month_last_day ():    
    day_last = date_today.replace(day=last_day())
    return day_last

def month_day(day):
    return date_today.replace(day = day)


shift_days = ("Monday", "Tuesday", "Wednesday", "Friday", "Saturday")
shifts = []
for x in range (month_first_day().day, last_day() + 1):
    name_weekday = month_day(x).strftime("%A")
    if name_weekday in shift_days:
        shifts.append(name_weekday)

 

def shifts_current_month():
    for x in range(month_first_day().day, today_decimal() + 1):
        x = month_day(x).strftime("%A %d, %B %Y")
        if "Monday" in x or "Tuesday" in x or "Wednesday" in x or "Friday" in x or "Saturday" in x:
            days.append(x)
    return days

def km_orders():
    global days
    total_km = 0
    total_orders = 0
    for y in days:
        daily_km = float(input("How much did you ride on {}: ".format(y)))
        daily_orders = float(input("How many delivers did you had on {}: ".format(y)))
        total_km = daily_km + total_km
        total_orders = daily_orders + total_orders
    return ("You have driven until {} {}km and had delivered {} orders".format(date_today.strftime("%A %d, %B %Y"), (total_km),(total_orders)))

print(shifts_current_month(), km_orders())