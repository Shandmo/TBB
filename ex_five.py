#!/usr/bin/python3
""" Exercise Five Simple Math """
num_one = input("Please enter your first number.\n> ")
num_two = input("Please enter your second  number.\n> ")
addition = (int(num_one) + int(num_two))
subtraction = (int(num_one) - int(num_two))
multiplication = (int(num_one) * int(num_two))
division = (int(num_one) / int(num_two))
print(f"{num_one} + {num_two} = {addition}\n{num_one} - {num_two} = {subtraction}\n \
{num_one} * {num_two} = {multiplication}\n {num_one} \ {num_two} = {division}")
