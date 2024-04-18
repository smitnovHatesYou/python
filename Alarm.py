current_time = input("What time is it right now?:  ")

print(current_time)

sleep_time = input ("How long would you like to sleep?:  ")

print(sleep_time)


alarm_time = int(current_time) + int(sleep_time) % 24

print("Your alarm will go off at " + str(alarm_time))