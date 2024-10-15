from datetime import date ,time, datetime
today = date.today()
n = datetime.now()

print("Today's date is ",today)
print("\nCurrent date and time is ",n)

print("\ndate components ",today.year,today.month,today.day)