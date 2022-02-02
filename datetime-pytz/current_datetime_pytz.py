#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos
import datetime,pytz
from datetime import date

#current date and time
current_date_time=datetime.datetime.now()
print(f"Current date and time in acutual format is {current_date_time}.")
#current date time in readable fromat
current_date_time_redable=current_date_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time in redable format is {current_date_time_redable}.")
#current date only 
current_date = "%s/%s/%s" %(current_date_time.year, current_date_time.month, current_date_time.day)
#current time only
current_time ="%s:%s:%s" %(current_date_time.hour,current_date_time.minute,current_date_time.second)
print(f"Current date is {current_date}.Current time is {current_time}.")

#Another method for current date
current_date=date.today()
#format dd/mm/YY
format1=current_date.strftime("%d/%m/%Y")
#format mm/dd/y
format2=current_date.strftime("%m/%d/%y")
#format month, day and year
format3=current_date.strftime("%B %d, %Y")
print(f"Format in dd/mm/yy is {format1}.")
print(f"Format in mm/dd/y is {format2}.")
print(f"Format in Day, Month and Year is {format3}.")

#current time for Tokyo
tokyo_current_time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
print(f"Current date and time for Tokyo in acutual format is {tokyo_current_time}.")
#current date time in readable fromat
tokyo_current_date_time_redable=tokyo_current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time in redable format is {tokyo_current_date_time_redable}.")
#Tokyo current date only 
tokyo_current_date = "%s/%s/%s" %(tokyo_current_time.year, tokyo_current_time.month, tokyo_current_time.day)
#Tokyo current time only
tokyo_current_time ="%s:%s:%s" %(tokyo_current_time.hour,tokyo_current_time.minute,tokyo_current_time.second)
print(f"Current date for Tokyo is {tokyo_current_date}.Current time for Tokyo is {tokyo_current_time}.")

