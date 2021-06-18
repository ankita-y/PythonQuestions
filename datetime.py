import datetime
print(datetime.date(2021,5,22))
# timedelta - It is used to manipulate data
# Current date and time
print(datetime.datetime.now())
# current date
print(datetime.date.today())
# to specify date in specific format
print(datetime.time())
now = datetime.datetime.now()
t = now.strftime("%d/%m/%Y")
print(t)
t1 = datetime.date.today()
# after 10 days
t2 = datetime.timedelta(days=20) 
t3 = t1+t2
print(t3)
# 10 days ago
t2 = datetime.timedelta(days=20) 
t3 = t1-t2
print(t3)
