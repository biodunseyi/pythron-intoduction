# Modules and Packages
import datetime
from datetime import date, datetime

# today = datetime.date.today()
today = date.today()

# print(f'Today date is {today}')
# time.sleep(4)
# print("Welcome")
# print(f'Today date is {today}')

formatted_date = today.strftime("%d-%m-%Y")

# print(formatted_date)

current_date_time = datetime.now()

current_time = current_date_time.time()
current_date = current_date_time.date()
formatted_date_time = current_date_time.strftime("%H:%M:%S %d-%m-%Y")
#print(current_date_time)
#print(formatted_date_time)

print(current_time)
print(current_date)

