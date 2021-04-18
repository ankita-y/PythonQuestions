# Tell the current day based on the provide date
from datetime import datetime as dt, date
import calendar as cl
week = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
date_txt = input("Enter date in format MM-DD-YYYY: ")
print(date_txt)
date_obj = dt.strptime(date_txt, "%m-%d-%Y")
date_year = date_obj.year
date_month = date_obj.month
date_day = date_obj.day

weekday = cl.weekday(date_year, date_month, date_day)
print(weekday)
if weekday in week:
    print(week[weekday])