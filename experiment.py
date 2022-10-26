from http.client import LENGTH_REQUIRED
import locale
from pydoc import locate
from datetime import datetime, date as dt
import calendar as cal

# loop = [2,56,54,78,99,65,982]

# max = loop[0]

# for x in loop:
#     if x > max:
#         max = x
# print(max)


locale.setlocale(locale.LC_ALL, 'de_DE')

date_today = datetime.now()
current_date = dt.today()

current_month = cal.monthcalendar(year = current_date.year, month = current_date.month)

largest_number = current_month[0][0]
for entry in current_month:
    for x in entry:
        if x >  largest_number:
            largest_number = x

print(largest_number)