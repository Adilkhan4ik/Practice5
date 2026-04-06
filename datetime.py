import datetime
now = datetime.datetime.now()
print(now)  # e.g., 2026-04-06 18:25:30

today = datetime.date.today()
print(today)  # e.g., 2026-04-06

d = datetime.date(2025, 12, 25)
t = datetime.time(15, 30, 45)

print(d)  # 2025-12-25
print(t)  # 15:30:45


now = datetime.datetime.now()

print(now.year)   # 2026
print(now.month)  # 4
print(now.day)    # 6
print(now.hour)   # 18
print(now.minute) # 25
print(now.second) # 30



now = datetime.datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)  # 06-04-2026 18:25:30




date_str = "25-12-2025"
date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
print(date_obj)  # 2025-12-25 00:00:00




today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)

print("Today:", today)
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)