str_seconds = input("Please enter the number of seconds you wish to convert:  ")

total_secs = int(str_seconds)

hours = total_secs // 3600

secs_still_remaining = total_secs % 3600

minutes = secs_still_remaining // 60

secs_still_remaining = secs_still_remaining % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_still_remaining)

