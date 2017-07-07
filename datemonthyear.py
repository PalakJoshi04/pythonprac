#display todays momth date and year separately
import datetime
currentDate = datetime.date.today()

print(currentDate.strftime('%d'))
print(currentDate.year)
print(currentDate.month)
print(currentDate.strftime('%d %B,%y'))

