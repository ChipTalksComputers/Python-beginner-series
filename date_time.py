#Dates and Times

import datetime

#current date and time
now = dtetime.datetime.now()

print(date)

#today's date and time
today = datetime.datetime.today()

print(today)

#Creating date and time

date = datetime.date(2020, 5, 28)

time = datetime.time(5, 20, 15)

print(date, time)

#Formatting
new_date = date.strftime("%d/%m/%Y")

new_time = date.strftim("%H:%M:%S:%f")

print(new_date, new_time)

#timedelta
time1 = datetime.timedelta(seconds = 55)

time2 = datetime.timedelta(seconds = 66)

print(time2 - time1)

date1 = datetime.timedelta(days = 11)

date2 = datetime.timedelta(days = 15)

print(date2 - date1)


