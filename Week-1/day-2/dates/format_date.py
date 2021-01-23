#To get current date and time we need to use the datetime library
from datetime import datetime

# The now function returns current date and time
today = datetime.now()

# use day, month, year, hour, minute, second functions
# to display only part of the date
# All these functions return integers
# Convert them to strings before concatenating them to another string
print('Date: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))

# Using the strftime() Method
print("DD/MM/YY: " + str(today.strftime('%d/%m/%y')))
print("DD Month YYYY: " + str(today.strftime('%d %B %Y')))
print("MM/DD/YYYY, H:M:S : " + str(today.strftime("%m/%d/%Y, %H:%M:%S")))
