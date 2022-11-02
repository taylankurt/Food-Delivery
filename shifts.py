from datetime import datetime as dt, date
import calendar as cal

date_today = dt.now()
current_date = date.today()
current_month_array = cal.monthcalendar(year = current_date.year, month = current_date.month)

def last_day(): # to determine the last day of the month
    largest_number = current_month_array[0][0]
    for entry in current_month_array:
        for x in entry:
            if x >  largest_number:
                largest_number = x
    return largest_number

def today_decimal(): # for range 
    return int(date_today.strftime("%d"))

def month_first_day ():
    date = date_today.replace(day=1)
    return date

def month_last_day ():    
    day_last = date_today.replace(day=last_day())
    return day_last

def month_day(day):
    return date_today.replace(day = day)

def current_distance_delivery():
    shift_days = []
    total_distance = 0
    total_deliveries = 0
    for x in range(month_first_day().day, today_decimal() + 1):
        x = month_day(x).strftime("%A %d, %B %Y")
        if "Monday" in x or "Tuesday" in x or "Wednesday" in x or "Friday" in x or "Saturday" in x:
            shift_days.append(x)
    for y in shift_days:
        daily_distance = float(input("How much did you ride on {}: ".format(y)))
        daily_delivery = float(input("How many delivers did you had on {}: ".format(y)))
        total_distance = daily_distance + total_distance
        total_deliveries = daily_delivery + total_deliveries
    return ("You have driven until {} {}km and had delivered {} orders".format(date_today.strftime("%A %d, %B %Y"), total_distance,total_deliveries))

print(current_distance_delivery())