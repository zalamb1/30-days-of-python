from datetime import datetime, date
#1
now=datetime.now()
print(now)
#2
t=now.strftime("%m/%D/%y, %H:%M:%S")
print("time: ",t)
#3
#date_string = "5 December, 2019"
#date_object = datetime.strptime(date_string, "%D %B,%Y")
#print("date_object =", date_object)     
#4
today = date(year=2026, month=9, day=23)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print("time left for new year: ", time_left_for_newyear)
#
time= date (year=1970 , month=1,day=1)
time_difrance=today-time
print("the time difrance is: ",time_difrance)