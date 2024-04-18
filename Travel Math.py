current_day = input("What day is it today?:  ")

print(current_day)

days_away = input ("How many days will you be gone?:  ")

print(days_away)


return_date = int(current_day) + int(days_away) % 7

print("You will return on " + str(return_date))