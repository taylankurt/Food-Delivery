from datetime import datetime as dt, date
import calendar as cal
import re
import os


class Month:
    def __init__(self):
        self.month_number = int(input(
            "Please enter the month in number(1-12): "))
        self.date_today = dt.now()
        self.current_date = date.today()

    def today_decimal(self):
        return int(self.date_today.strftime("%d"))

    def first_day_decimal(self):
        first_day = self.date_today.replace(month=self.month_number, day=1)
        return first_day.day

    def first_day(self, day):
        self.day = day
        date_x = self.date_today.replace(
            month=self.month_number, day=day).strftime("""%A %d, %B %Y""")
        return date_x

    def last_day_decimal(self):  # to determine the last day of the month
        current_month_array = cal.monthcalendar(
            year=self.current_date.year, month=self.month_number)
        largest_number = 0
        for entry in current_month_array:
            for x in entry:
                if x > largest_number:
                    largest_number = x
        return largest_number

    def shifts_month(self):
        shifts = []
        for decimal_day in range(self.first_day_decimal(), self.today_decimal() + 1):
            fullday = self.first_day(decimal_day)
            if "Monday" in fullday or "Tuesday" in fullday or "Wednesday" in fullday or "Friday" in fullday or "Saturday" in fullday:
                shifts.append(fullday)
        return shifts

    def shifts_month_decimal(self):
        shifts_decimal = []
        for decimal_day in range(self.first_day_decimal(), self.today_decimal() + 1):
            fullday = self.first_day(decimal_day)
            if "Monday" in fullday or "Tuesday" in fullday or "Wednesday" in fullday or "Friday" in fullday or "Saturday" in fullday:
                selected_shift = self.date_today.replace(
                    month=self.month_number, day=decimal_day).strftime("%d %m %Y")
                shifts_decimal.append(selected_shift)
        return shifts_decimal

    def current_distance_delivery(self):
        os.system("clear")
        filename = "data.txt"

        if not os.path.isfile(filename):
            with open(filename, "w") as data_file:
                data_file.write("Date;Kilometer;Deliveries" + "\n")

        with open(filename, "r+") as data_file:
            lines = data_file.readlines()
            entry_found = False

            for x in self.shifts_month_decimal():
                entry_found = False
                for sentence in lines:
                    if x in sentence:
                        print("The distance data for {} is already written".format(x))
                        entry_found = True

                if entry_found == False:
                    daily_distance = float(input(
                        "How much did you ride on {}: ".format(x)))
                    daily_delivery = float(input(
                        "How many delivers did you had on {}: ".format(x)))
                    with open("data.txt", "a+") as data_file:
                        data_file.write(
                            str("""{};{};{}""".format(x, int(daily_distance), int(daily_delivery))) + "\n")


# total_distance = 0
# total_deliveries = 0
# total_distance = daily_distance + total_distance
# total_deliveries = daily_delivery + total_deliveries
# av_deliveries = total_deliveries / len(self.shifts_month_decimal())
# av_distance = total_distance / len(self.shifts_month_decimal())
mjam = Month()
print(mjam.current_distance_delivery())
