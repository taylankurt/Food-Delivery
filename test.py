from datetime import datetime as dt, date
import calendar as cal
import os
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage
from credentials import gmailAppPassword


class Mjam:

    currentDate = date.today()

    def __init__(self):
        self.dateToday = dt.now()
        self.currentDate = date.today()
        self.monthNumber = self.currentDate.month
        self.month = int(input("Please enter the month in number(1-12): "))

    def todayDecimal(self, month=currentDate.month):
        return int(self.dateToday.replace(month=month).strftime("%d"))

    def firstDayDecimal(self, month=currentDate.month):
        firstDay = self.dateToday.replace(month=month, day=1)
        return firstDay.day

    def firstDay(self, day, month=currentDate.month):
        self.day = day
        firstDay = self.dateToday.replace(
            month=month, day=day).strftime("""%A %d, %B %Y""")
        return firstDay

    # to determine the last day of the month
    def lastDayDecimal(self, month=currentDate):
        currentMonthArray = cal.monthcalendar(
            year=self.currentDate.year, month=month)
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

    def shiftsMonthDecimal(self, month=currentDate.month):
        shiftsDecimal = []
        if month == self.currentDate.month:
            for decimalDay in range(self.firstDayDecimal(month), self.todayDecimal(month) + 1):
                fullday = self.firstDay(decimalDay, month)
                if "Monday" in fullday or "Tuesday" in fullday or "Wednesday" in fullday or "Friday" in fullday or "Saturday" in fullday:
                    selectedShift = self.dateToday.replace(
                        month=month, day=decimalDay).strftime("%d-%m-%Y")
                    shiftsDecimal.append(selectedShift)
        else:
            for decimalDay in range(self.firstDayDecimal(month), self.lastDayDecimal(month) + 1):
                fullday = self.firstDay(decimalDay, month)
                if "Monday" in fullday or "Tuesday" in fullday or "Wednesday" in fullday or "Friday" in fullday or "Saturday" in fullday:
                    selectedShift = self.dateToday.replace(
                        month=month, day=decimalDay).strftime("%d-%m-%Y")
                    shiftsDecimal.append(selectedShift)

        return shiftsDecimal

    def writeCurrentMonth(self):
        os.system("clear")
        filename1 = "data.csv"
        filename2 = "absence.csv"

        if not os.path.isfile(filename1):
            with open(filename1, "w") as dataFile:
                dataFile.write("Date;Kilometer;Deliveries;Tipp" + "\n")

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
                    dailyTipp = float(
                        input("How much Tipp did you had on {}: ".format(x)))
                    with open(filename1, "a+") as dataFile:
                        dataFile.write(
                            str("""{};{};{};{}""".format(x, round(dailyDistance, 2), int(dailyDelivery), (dailyTipp))) + "\n")
        return ""

    def writeGivenMonth(self):
        os.system("clear")
        filename1 = "data.csv"
        filename2 = "absence.csv"

        if not os.path.isfile(filename1):
            with open(filename1, "w") as dataFile:
                dataFile.write("Date;Kilometer;Deliveries;Tipp" + "\n")

        with open(filename1, "r+") as dataFile, open(filename2, "r+") as absenceFile:
            lines = dataFile.readlines()
            lines2 = absenceFile.readlines()
            entryFound = False
            for x in self.shiftsMonthDecimal(month=self.month):
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
                    dailyTipp = float(
                        input("How much Tipp did you had on {}: ".format(x)))
                    with open(filename1, "a+") as dataFile:
                        dataFile.write(
                            str("""{};{};{};{}""".format(x, round(dailyDistance, 2), int(dailyDelivery), (dailyTipp))) + "\n")
        return ""

    def dataAnalysis(self):
        os.system("clear")
        filename = "data.csv"
        dateData = []
        kilometerData = []
        deliveryData = []
        TippData = []
        totalDistance = 0
        totalDeliveries = 0
        totalTipp = 0
        currentMonth = self.currentDate.replace(
            month=self.month).strftime("%B %Y")
        firstLine = True

        with open(filename) as dataFile:
            lines = dataFile.readlines()
            for line in lines:
                if firstLine == True:
                    firstLine = False
                    continue
                splitArray = line.split(";")
                dateArray = splitArray[0].split("-")
                if str(self.month) in dateArray[1]:
                    dateData.append(dateArray[0:2])
                    kilometerData.append(splitArray[1])
                    deliveryData.append(splitArray[2])
                    TippData.append(splitArray[3])

        for day in kilometerData:
            totalDistance = totalDistance + float(day)
        for day in deliveryData:
            totalDeliveries = totalDeliveries + float(day)
        for day in TippData:
            totalTipp = totalTipp + float(day)

        avDeliveriesDay = totalDeliveries / len(deliveryData)
        avDeliveriesHour = avDeliveriesDay / 5
        avDistance = totalDistance / len(kilometerData)
        avTipp = totalTipp / len(TippData)
        workedDays = len(dateData)

        return f"""Your data for {currentMonth} is:\n\n\nWorked Days:{workedDays}\n\nTotal Distance: {round(totalDistance, 1)}km\n
Distance Average: {round(avDistance, 2)}km\n\nTotal Deliveries: {int(totalDeliveries)}\n
Delivery Average(Day): {round(avDeliveriesDay, 2)}\n\nDelivery Average(Hour): {round(avDeliveriesHour, 2)}\n
Total Tipp: {totalTipp} €\n\nTipp Average: {round(avTipp, 2)} €\n\nNice job :)"""

    def dataGraph(self):
        os.system("clear")
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
                if str(self.month) in splitArray[0][3:5]:
                    kilometer.append(kilometerLine)
                    date.append(dateLine)
                    delivery.append(deliveryLine)

        x = date
        y = delivery
        plt.bar(x, y)
        label = "Date for month: " + str(self.monthNumber)

        plt.xlabel(label)
        plt.ylabel("Delivery")
        plt.title("Work Graph")

        return plt.show()

    def emailData(self):
        os.system("clear")
        currentMonth = self.currentDate.replace(
            month=self.month).strftime("%B %Y")
        msg = EmailMessage()
        msg.set_content(self.dataAnalysis())
        password = gmailAppPassword

        msg['Subject'] = 'Mjam Work Data for {}'.format(currentMonth)
        msg['From'] = "taylankurtyedek@gmail.com"
        msg['To'] = "kurt.taylan@icloud.com"

        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("taylankurtyedek@gmail.com", password)
        server.send_message(msg)
        server.quit()
        return "Message sent"


Taylan = Mjam()

print(Taylan.dataAnalysis())
