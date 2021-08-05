phone_no = int(input("Enter the number here: "))
message = input("Enter the message here: ")
time_hour = int(input("Enter the time in hours: "))
time_min = int(input("Enter the time in min: "))

import pywhatkit
pywhatkit.sendwhatmsg(f'+91{phone_no}', message, time_hour,time_min)