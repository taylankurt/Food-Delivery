from datetime import datetime as dt, date
import calendar as cal
import os
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage
from credentials import appPasswordGmailYedek


class Mjam:

    currentDate = date.today()

    def __init__(self):
        self.dateToday = dt.now()
        self.currentDate = date.today()
        self.monthNumber = self.currentDate.month
        self.selectedMonth = int(
            input("Please enter the month in number(1-12): "))
        self.selectedYear = int(
            input("Please enter the year in full year(e.g.: 2022): "))

    def todayDecimal(self, month=currentDate.month):
        return int(self.dateToday.replace(month=month).strftime("%d"))

    def firstDayDecimal(self, month=currentDate.month, year=currentDate.year):
        firstDay = self.dateToday.replace(year=year, month=month, day=1)
        return firstDay.day

    def firstDay(self, day, month=currentDate.month, year=currentDate.year):
        self.day = day
        firstDay = self.dateToday.replace(
            year=year, month=month, day=day).strftime("""%A %d, %B %Y""")
        return firstDay

    # to determine the last day of the month
    def lastDayDecimal(self, month=currentDate, year=currentDate.year):
        currentMonthArray = cal.monthcalendar(
            year=year, month=month)
        largestNumber = 0
        for entry in currentMonthArray:
            for x in entry:
                if x > largestNumber:
                    largestNumber = x
        return largestNumber

    def absenceMonth(self):
        os.system("clear")
        absenceDay = True
        path = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/absence.csv"

        if not os.path.isfile(path):
            with open(path, "w") as dataFile:
                dataFile.write("Date" + "\n")

        while absenceDay:
            os.system("clear")
            print("""To exit press "e" """)
            line = input("Absence date(e.g. 01 01 2023): ").split(' ')
            date = []
            for x in line:
                if x.isdigit():
                    date.append(x)
                elif x == "e":
                    absenceDay = False
                    print("Exiting")
                    break
            if absenceDay == True:
                with open(path, "a+") as absenceFile:
                    absenceFile.write(str("{}-{}-{}\n").format(
                        date[0], date[1], date[2]))
        return ""

    def shiftsMonthDecimal(self, month=currentDate.month, year=currentDate.year):
        os.system("clear")
        shiftsDecimal = []
        if month == self.currentDate.month and year == self.currentDate.year:
            for decimalDay in range(self.firstDayDecimal(month, year), self.todayDecimal(month) + 1):
                fullday = self.firstDay(decimalDay, month, year)
                if "Monday" in fullday or "Tuesday" in fullday or "Wednesday" in fullday or "Friday" in fullday or "Saturday" in fullday:
                    selectedShift = self.dateToday.replace(
                        year=year, month=month, day=decimalDay).strftime("%d-%m-%Y")
                    shiftsDecimal.append(selectedShift)
        else:
            for decimalDay in range(self.firstDayDecimal(month, year), self.lastDayDecimal(month, year) + 1):
                fullday = self.firstDay(decimalDay, month, year)
                if "Monday" in fullday or "Tuesday" in fullday or "Wednesday" in fullday or "Friday" in fullday or "Saturday" in fullday:
                    selectedShift = self.dateToday.replace(
                        year=year, month=month, day=decimalDay).strftime("%d-%m-%Y")
                    shiftsDecimal.append(selectedShift)

        return shiftsDecimal

    def writeCurrentMonth(self):
        os.system("clear")
        filename1 = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/data.csv"
        filename2 = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/absence.csv"
        path = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/data.csv"

        if not os.path.isfile(path):
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
        filename1 = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/data.csv"
        filename2 = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/absence.csv"
        path = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/data.csv"

        if not os.path.isfile(path):
            with open(filename1, "w") as dataFile:
                dataFile.write("Date;Kilometer;Deliveries;Tipp" + "\n")

        with open(filename1, "r+") as dataFile, open(filename2, "r+") as absenceFile:
            lines = dataFile.readlines()
            lines2 = absenceFile.readlines()
            entryFound = False
            for x in self.shiftsMonthDecimal(month=self.selectedMonth, year=self.selectedYear):
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
        os.system('cls')
        path = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/data.csv"
        dateData = []
        kilometerData = []
        deliveryData = []
        TippData = []
        totalDistance = 0
        totalDeliveries = 0
        totalTipp = 0
        currentMonth = self.currentDate.replace(
            year=self.selectedYear, month=self.selectedMonth).strftime("%B %Y")
        firstLine = True

        with open(path) as dataFile:
            lines = dataFile.readlines()
            for line in lines:
                if firstLine == True:
                    firstLine = False
                    continue
                splitArray = line.split(";")
                dateArray = splitArray[0].split("-")
                if str(self.selectedMonth) in dateArray[1] and str(self.selectedYear) in dateArray[2]:
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
        os.system("cls")
        date = []
        kilometer = []
        delivery = []
        path = "C:/Users/tayla/iCloudDrive/Documents/Arbeit/UserDaten/data.csv"

        firstLine = True

        with open(path, "r+") as dataFile:
            lines = dataFile.readlines()
            for line in lines:
                if firstLine == True:
                    firstLine = False
                    continue

                splitArray = line.split(";")
                dateLine = str(splitArray[0][:2])
                kilometerLine = float(splitArray[1])
                deliveryLine = float(splitArray[2].rstrip("\n"))
                if str(self.selectedMonth) in splitArray[0][3:5] and str(self.selectedYear) in splitArray[0][6:10]:
                    kilometer.append(kilometerLine)
                    date.append(dateLine)
                    delivery.append(deliveryLine)

        x = date
        y = delivery
        plt.bar(x, y)
        label = "Month: " + self.currentDate.replace(
            month=self.selectedMonth).strftime("%B")

        plt.xlabel(label)
        plt.ylabel("Delivery")
        plt.title("Work Graph")

        return plt.show()

    def emailData(self):
        os.system("clear")
        currentMonth = self.currentDate.replace(
            year=self.selectedYear, month=self.selectedMonth).strftime("%B %Y")
        msg = EmailMessage()
        msg.set_content(self.dataAnalysis())
        password = appPasswordGmailYedek

        msg['Subject'] = "Mjam Work Data for {}".format(currentMonth)
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
