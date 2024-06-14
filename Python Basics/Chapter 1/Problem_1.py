# Solution

# Ask for current time in hours
current_time = int(input('What time is it now (in hours, 0-23)?: '))

# Ask for number of hours to wait until alarm goes off
waiting_time = int(input('After how many hours would you like to wake up?: '))

# Calculate the time when the alarm goes off
alarm_time = (current_time + waiting_time) % 24

# Output the result
print(f'The alarm will go off at {alarm_time}:00')

