import datetime
hour = datetime.datetime.now().hour
if hour < 12:
    print("Good morning")
if hour < 17:
    print("Good afternoon")
else:
    print("Good evening")