#!/usr/bin/python3
""" Exercise Six Retirement Calculator """
from datetime import date
today = date.today()
this_year = today.strftime("%Y")
age = input("What is your current age?\n> ")
retire_age = input("What age would you like to retire?\n> ")
time_left = (int(retire_age) - int(age))
retire_year = (int(this_year) + int(time_left))
print(f"You have {time_left} years left until you can retire.")
print(f"It's {this_year}, so you can retire in {retire_year}.")
