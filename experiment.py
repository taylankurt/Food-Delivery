from datetime import datetime as dt, date
import calendar as cal
import os

shifts = []


class Month:
    def __init__(self):
        self.month_number = int(input(
            "Please enter the month in number(1-12): "))

    def today_decimal(self):
        date_today = dt.now()
        return int(date_today.strftime("%d"))

    def first_day_decimal(self):
        month = self.month_number
        date_today = dt.now()
        date_x = date_today.replace(month=month, day=1)
        return date_x.day

    def first_day(self, day):
        self.day = day
        month = self.month_number
        date_today = dt.now()
        date_x = date_today.replace(
            month=month, day=day).strftime("%A %d, %B %Y")
        return date_x

    def last_day_decimal(self):  # to determine the last day of the month
        month = self.month_number
        current_date = date.today()
        current_month_array = cal.monthcalendar(
            year=current_date.year, month=month)
        largest_number = 0
        for entry in current_month_array:
            for x in entry:
                if x > largest_number:
                    largest_number = x
        return largest_number

    def shifts_month(self):
        for x in range(self.first_day_decimal(), self.today_decimal() + 1):
            dayname = self.first_day(x)
            if "Monday" in dayname or "Tuesday" in dayname or "Wednesday" in dayname or "Friday" in dayname or "Saturday" in dayname:
                shifts.append(dayname)
        return shifts

    def current_distance_delivery(self):
        date_today = dt.now()
        os.system("clear")
        total_distance = 0
        total_deliveries = 0
        for x in self.shifts_month():
            daily_distance = float(
                input("How much did you ride on {}: ".format(x)))
            daily_delivery = float(
                input("How many delivers did you had on {}: ".format(x)))
            total_distance = daily_distance + total_distance
            total_deliveries = daily_delivery + total_deliveries
        return ("You have driven until {} {}km and had delivered {} orders".format(date_today.strftime("%A %d, %B %Y"), total_distance, int(total_deliveries)))


# def shifts_month():
#     selected_month = int(input("Please enter the month in number(1-12): "))
#     month = Month(selected_month)
#     for x in range(month.first_day_decimal(), month.today_decimal() + 1):
#         x = month.first_day(x)
#         if "Monday" in x or "Tuesday" in x or "Wednesday" in x or "Friday" in x or "Saturday" in x:
#             shifts.append(x)
#     return shifts


# def current_distance_delivery():
#     os.system("cls")
#     total_distance = 0
#     total_deliveries = 0
#     for x in shifts_month():
#         daily_distance = float(
#             input("How much did you ride on {}: ".format(x)))
#         daily_delivery = float(
#             input("How many delivers did you had on {}: ".format(x)))
#         total_distance = daily_distance + total_distance
#         total_deliveries = daily_delivery + total_deliveries
#     return ("You have driven until {} {}km and had delivered {} orders".format(date_today.strftime("%A %d, %B %Y"), total_distance, int(total_deliveries)))

mjam = Month()
print(mjam.current_distance_delivery())
