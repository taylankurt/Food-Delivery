import datetime
from datetime import date
import calendar
from test import month_first_day, month_last_day, today_decimal, last_day

date_today = datetime.datetime.now()
current_date = date.today

def today_decimal():
    return int(date_today.strftime("%d"))

# print(type(today_decimal()))

next_date = datetime.datetime.today() + datetime.timedelta(days =1)
next_date_formatted = next_date.strftime("%A %d, %B %Y")

# def km_month():
#     for x in range(1,today_decimal() +1):
#         month_first_day = 
#         daily_km = int(input("How much did you ride on {}: ".format(month_first_day())))
#         daily_km = next_date = datetime.datetime.today() - datetime.timedelta(days = 1)
#         print(daily_km)

# month_first_day =  next_date = datetime.datetime.today() - datetime.timedelta(days = 1)
print(next_date_formatted)
