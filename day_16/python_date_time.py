# Import the datetime module for working with dates and times
from datetime import datetime

# Get the current date and time
now = datetime.now()
print("Now:", now)  # Print the full current date and time

# Extract individual components of the current date and time
day = now.day  # Get the day of the month
month = now.month  # Get the month (1-12)
year = now.year  # Get the year
hour = now.hour  # Get the hour (0-23)
minute = now.minute  # Get the minute (0-59)
second = now.second  # Get the second (0-59)
timestamp = now.timestamp()  # Get the timestamp (seconds since epoch)

# Print the extracted components
print('Current day:', day)
print('Current month:', month)
print('Current year:', year)
print('Current hour:', hour)
print('Current minute:', minute)
print('Current second:', second)
print('Current timestamp:', timestamp)  # Print the Unix timestamp

# Format the current date and time as a string in a specific format
current_date = now.strftime("%m/%d/%Y, %H:%M:%S")  # Format: MM/DD/YYYY, HH:MM:SS
print(current_date)  # Print the formatted current date and time

# Parse a specific date string into a datetime object
date_string = "17 December, 2024"  # Define a date in string format
time_string = datetime.strptime(date_string, "%d %B, %Y")  # Convert string to datetime object
print("date_object =", time_string)  # Print the parsed datetime object

# Create a datetime object for a specific date
now = datetime(year=2024, month=12, day=17)  # Define a specific date (17th December 2024)
new_year = datetime(year=2025, month=1, day=1)  # Define the New Year (1st January 2025)

# Calculate the difference between the two dates
time_difference = new_year - now  # Calculate the timedelta between the dates
print("Time difference:", time_difference)  # Print the difference (days, hours, etc.)