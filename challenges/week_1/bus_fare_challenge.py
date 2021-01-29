from datetime import date

date = date.today()

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
if day in bus_fare:
    print(date)
    print(day)
    fare = bus_fare[day]
    print(fare)
