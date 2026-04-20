# Author: Antonio Loureiro Dunch
# GitHub username: aloureirodunch
# Date: April 16th, 2026
# Description: Converts seconds into hours, minutes, and seconds.

seconds = int(input("Enter a number of seconds: "))

hours = seconds // 3600

minutes = (seconds % 3600) // 60

remainingseconds = seconds % 60

print(f"{seconds} seconds is equal to {hours} hours, {minutes} minutes and {remainingseconds} seconds,")