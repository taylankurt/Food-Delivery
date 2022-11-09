from datetime import datetime as dt, date
import calendar as cal

date_today = dt.now()
current_date = date.today()
current_month_array = cal.monthcalendar(
    year=current_date.year, month=current_date.month)
shift_name = ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday"]
shifts = []


def last_day():  # to determine the last day of the month
    largest_number = current_month_array[0][0]
    for entry in current_month_array:
        for x in entry:
            if x > largest_number:
                largest_number = x
    return largest_number


def today_decimal():  # for range
    return int(date_today.strftime("%d"))


def month_first_day():
    date = date_today.replace(day=1)
    return date


def month_last_day():
    day_last = date_today.replace(day=last_day())
    return day_last


def month_day(day):
    return date_today.replace(day=day)


def shift_name_month():
    for x in range(month_first_day().day, today_decimal() + 1):
        dayname = month_day(x).strftime("%A")
        day = month_day(x).strftime("%A %d, %B %Y")
        if dayname in shift_name:
            shifts.append(day)
    return shifts


def current_distance_delivery():
    total_distance = 0
    total_deliveries = 0
    for x in shift_name_month():
        daily_distance = float(
            input("How much did you ride on {}: ".format(x)))
        daily_delivery = float(
            input("How many delivers did you had on {}: ".format(x)))
        total_distance = daily_distance + total_distance
        total_deliveries = daily_delivery + total_deliveries
    return ("You have driven until {} {}km and had delivered {} orders".format(date_today.strftime("%A %d, %B %Y"), total_distance, int(total_deliveries)))


print(current_distance_delivery())
