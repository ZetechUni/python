# WRITE YOUR CODE SOLUTION HERE
from datetime import datetime, timedelta, date

#Get todays date and store it in a variable 'date'

date = datetime.now()

"""
# Use todays date to get the name on the day of the week written in a short 
# form with the first letter capitalized (e.g) 'Fri' if today were Friday and 
# assigns it a variable 'day'
"""
day = datetime.date(date).strftime('%a')


"""
Uses if Statement to determine the todays fare following these bus fare shedule:
    Monday - Friday --> 100
    Saturdat --> 60
    Sunday --> 80

Prints the results in this exact formart
    Date: 2021-01-05
    Day:Tue
    Fare:100

"""
if day == "Mon" or day == "Tue" or day == "Wen" or day =="Thu" or day == "Fri":
    print("Date:", date)
    print("Day:" + day)
    print('Fare: 100')
elif day == "Sat":
    print("Date:", date)
    print("Day:" + day)
    print('fare:60')
else: 
    print("Date:", date)
    print("Day:" + day)
    print('fare:80')
