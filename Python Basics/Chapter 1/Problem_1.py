# Function to convert 24-hour time to 12-hour time with AM/PM
def convert_to_12_hour_format(hour):
    if hour == 0:
        return 12, "AM"  # Midnight case
    elif hour == 12:
        return 12, "PM"  # Noon case
    elif hour < 12:
        return hour, "AM"  # Morning case
    else:
        return hour - 12, "PM"  # Afternoon and evening case

# Ask for current time in hours
current_time = int(input('What time is it now (in hours, 0-23)?: '))

# Ask for number of hours to wait until alarm goes off
waiting_time = int(input('After how many hours would you like to wake up?: '))

# Calculate the time when the alarm goes off in 24-hour format
alarm_time_24_hour = (current_time + waiting_time) % 24

# Convert the 24-hour time to 12-hour time with AM/PM
converted_time_hour, period = convert_to_12_hour_format(alarm_time_24_hour)

# Output the result
print(f'The alarm will go off at {alarm_time_24_hour}:00 (24-hour format) or {converted_time_hour}:00 {period} (12-hour format)')
