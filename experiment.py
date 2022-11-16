from datetime import datetime as dt, date
import calendar as cal
import os

date_today = dt.now()
current_date = date.today()
current_month_array = cal.monthcalendar(
    year=current_date.year, month=current_date.month)
shifts = []


class Month:
    def __init__(self, month_number):
        self.month = month_number = int(input(
            "Please enter the month in number(1-12): "))

    def today_decimal(self):
        return int(date_today.strftime("%d"))

    def first_day_decimal(self):
        month = self.month
        date_today = dt.now()
        date = date_today.replace(month=month, day=1)
        return date.day

    def first_day(self, day):
        self.day = day
        month = self.month
        date_today = dt.now()
        date = date_today.replace(
            month=month, day=day).strftime("%A %d, %B %Y")
        return date

    def last_day_decimal(self):  # to determine the last day of the month
        month = self.month
        current_date = date.today()
        current_month_array = cal.monthcalendar(
            year=current_date.year, month=month)
        largest_number = 0
        for entry in current_month_array:
            for x in entry:
                if x > largest_number:
                    largest_number = x
        return largest_number

    def shifts_mjam(self):
        for x in range(month.first_day_decimal(), month.today_decimal() + 1):
            x = month.first_day(x)
            if "Monday" in x or "Tuesday" in x or "Wednesday" in x or "Friday" in x or "Saturday" in x:
                shifts.append(x)
        return shifts

    def current_distance_delivery(self):
        os.system("cls")
        total_distance = 0
        total_deliveries = 0
        for x in shifts_month():
            daily_distance = float(
                input("How much did you ride on {}: ".format(x)))
            daily_delivery = float(
                input("How many delivers did you had on {}: ".format(x)))
            total_distance = daily_distance + total_distance
            total_deliveries = daily_delivery + total_deliveries
        return ("You have driven until {} {}km and had delivered {} orders".format(date_today.strftime("%A %d, %B %Y"), total_distance, int(total_deliveries)))


print(month.shifts_month())
