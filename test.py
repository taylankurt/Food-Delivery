from datetime import datetime as dt, date
import calendar as cal
from itertools import islice
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
        first_day = self.date_today.replace(
            month=self.month_number, day=day).strftime("""%A %d, %B %Y""")
        return first_day

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
        filename = "data.csv"

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
                    with open(filename, "a+") as data_file:
                        data_file.write(
                            str("""{};{};{}""".format(x, round(daily_distance, 2), int(daily_delivery))) + "\n")

    def data(self):
        os.system("clear")
        total_distance = 0
        filename = "data.csv"
        date_data = []
        kilometer_data = []
        delivery_data = []
        total_distance = 0
        total_deliveries = 0
        current_month = self.current_date.replace(
            month=self.month_number).strftime("%B %Y")

        with open(filename) as data_file:
            for lines in islice(data_file, 1, None):
                date_data.append(lines[0:10])
                kilometer_data.append(lines[11:15])
                delivery_data.append(lines[17:19])
            data_file.close()

        for day in kilometer_data:
            total_distance = total_distance + float(day)
        for day in delivery_data:
            total_deliveries = total_deliveries + float(day)
        av_deliveries_day = total_deliveries / len(delivery_data)
        av_deliveries_hour = av_deliveries_day / 5
        av_distance = total_distance / len(kilometer_data)
        # print(delivery_data)

        return """Your data for {}:\nTotal Distance: {}km\nDistance Average: {}km\nTotal Deliveries: {}
Delivery Average(Day): {}\nDelivery Average(Hour): {}
""".format(current_month, round(total_distance, 1), round(av_distance, 2), int(total_deliveries), round(av_deliveries_day, 2), round(av_deliveries_hour, 2))


# total_distance = daily_distance + total_distance
# total_deliveries = daily_delivery + total_deliveries

mjam = Month()
print(mjam.data())
