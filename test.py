from datetime import datetime as dt, date
import calendar as cal
from itertools import islice
import os
import matplotlib.pyplot as plt


class Month:
    def __init__(self):
        self.monthNumber = int(input(
            "Please enter the month in number(1-12): "))
        self.dateToday = dt.now()
        self.currentDate = date.today()

    def todayDecimal(self):
        return int(self.dateToday.strftime("%d"))

    def firstDayDecimal(self):
        firstDay = self.dateToday.replace(month=self.monthNumber, day=1)
        return firstDay.day

    def firstDay(self, day):
        self.day = day
        firstDay = self.dateToday.replace(
            month=self.monthNumber, day=day).strftime("""%A %d, %B %Y""")
        return firstDay

    def lastDayDecimal(self):  # to determine the last day of the month
        currentMonthArray = cal.monthcalendar(
            year=self.currentDate.year, month=self.monthNumber)
        largestNumber = 0
        for entry in currentMonthArray:
            for x in entry:
                if x > largestNumber:
                    largestNumber = x
        return largestNumber

    def absenceMonth(self):
        os.system("clear")
        filename = "absence.csv"
        absenceDay = True

        if not os.path.isfile(filename):
            with open(filename, "w") as dataFile:
                dataFile.write("Date" + "\n")

        while absenceDay:
            line = input("Absence date: ").split(' ')
            date = []
            for x in line:
                if x.isdigit():
                    date.append(x)
                else:
                    absenceDay = False
                    break
            if absenceDay == True:
                with open(filename, "a+") as absenceFile:
                    absenceFile.write(str("{}-{}-{}\n").format(
                        date[0], date[1], date[2]))
        return date

    def shiftsMonthDecimal(self):
        shiftsDecimal = []
        for decimalDay in range(self.firstDayDecimal(), self.todayDecimal() + 1):
            fullday = self.firstDay(decimalDay)
            if "Monday" in fullday or "Tuesday" in fullday or "Wednesday" in fullday or "Friday" in fullday or "Saturday" in fullday:
                selectedShift = self.dateToday.replace(
                    month=self.monthNumber, day=decimalDay).strftime("%d-%m-%Y")
                shiftsDecimal.append(selectedShift)
        return shiftsDecimal

    def currentDistanceDelivery(self):
        os.system("clear")
        filename1 = "data.csv"
        filename2 = "absence.csv"
        if not os.path.isfile(filename1):
            with open(filename1, "w") as dataFile:
                dataFile.write("Date;Kilometer;Deliveries" + "\n")

        with open(filename1, "r+") as dataFile, open(filename2, "r+") as absenceFile:
            lines = dataFile.readlines()
            lines2 = absenceFile.readlines()
            entryFound = False

            for x in self.shiftsMonthDecimal():
                entryFound = False
                for sentence in lines:
                    if x in sentence:
                        print("The data for {} is already written".format(x))
                        entryFound = True

                for sentence in lines2:
                    if x in sentence:
                        print("You have not worked on {}".format(x))
                        entryFound = True

                if entryFound == False:
                    dailyDistance = float(input(
                        "How much did you ride on {}: ".format(x)))
                    dailyDelivery = float(input(
                        "How many delivers did you had on {}: ".format(x)))
                    with open(filename1, "a+") as dataFile:
                        dataFile.write(
                            str("""{};{};{}""".format(x, round(dailyDistance, 2), int(dailyDelivery))) + "\n")

    def dataAnalysis(self):
        os.system("clear")
        filename = "data.csv"
        dateData = []
        kilometerData = []
        deliveryData = []
        totalDistance = 0
        totalDeliveries = 0
        currentMonth = self.currentDate.replace(
            month=self.monthNumber).strftime("%B %Y")

        with open(filename) as dataFile:
            for lines in islice(dataFile, 1, None):
                dateData.append(lines[0:10])
                kilometerData.append(lines[11:15])
                deliveryData.append(lines[17:19])
            dataFile.close()

        for day in kilometerData:
            totalDistance = totalDistance + float(day)
        for day in deliveryData:
            totalDeliveries = totalDeliveries + float(day)

        avDeliveriesDay = totalDeliveries / len(deliveryData)
        avDeliveriesHour = avDeliveriesDay / 5
        avDistance = totalDistance / len(kilometerData)

        return """Your data for {}:\nTotal Distance: {}km\nDistance Average: {}km\nTotal Deliveries: {}
Delivery Average(Day): {}\nDelivery Average(Hour): {}""".format(currentMonth, round(totalDistance, 1), round(avDistance, 2),
                                                                int(totalDeliveries), round(avDeliveriesDay, 2), round(avDeliveriesHour, 2))

    def dataGraph(self):
        date = []
        kilometer = []
        delivery = []
        filename = "data.csv"
        firstLine = True

        with open(filename, "r+") as dataFile:
            lines = dataFile.readlines()
            for line in lines:
                if firstLine == True:
                    firstLine = False
                    continue

                splitArray = line.split(";")
                dateLine = str(splitArray[0][:2])
                kilometerLine = float(splitArray[1])
                deliveryLine = float(splitArray[2].rstrip("\n"))
                kilometer.append(kilometerLine)
                date.append(dateLine)
                delivery.append(deliveryLine)

        x = date
        y = delivery
        print(date)
        print("END")
        print(delivery)

        plt.bar(x, y,)
        label = "Date for month: " + str(self.monthNumber)

        plt.xlabel(label)
        plt.ylabel("Delivery")
        plt.title("Mjam Work Graph")

        return plt.show()

    def is_float_digit(self, x: str, y: str, z: str) -> bool:
        try:
            float(x)
            float(y)
            float(z)
            return True
        except ValueError:
            return False


mjam = Month()
print(mjam.dataGraph())
