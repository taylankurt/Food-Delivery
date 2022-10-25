from datetime import datetime
import calendar 

now = datetime.now()
current_time = now.strftime("%H:%M")
print(current_time)

x = calendar.weekheader(9).split()
for y in x:
    print(y)
    
today = datetime.today()
current_month = today.strftime("%m")
print(current_month)