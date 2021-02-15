from datetime import date
#initialize the date today
date = date.today()

#obtain the day in the form "Mon", "Tue" etc.
day = date.strftime("%a")

bus_fare = {
    "Mon":100,
    "Tue":100,
    "Wen":100,
    "Thur":100,
    "Fri":100,
    "Sat":60,
    "Sun":80
}
#initialize the fare variable
fare = None
#check if the day is in the bus_fare dictionary
if day in bus_fare:
    print(date)
    print(day)
    fare = bus_fare[day]
    print(fare)


