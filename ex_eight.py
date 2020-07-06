#!/usr/bin/python3
""" Exercise Eight Pizza Party """
import math

def main():
    """ Make function that handles remaining pizza"""
    people_num = input("How many people?\n> ")
    pizza_num = input("How many pizzas do you have\n> ")
    slices_num = (int(pizza_num) * 8)
    slices_per_person = math.floor((int(slices_num) / int(people_num)))
    remainder_slices = slices_num % int(people_num)
    print(f"{people_num} people with {pizza_num} pizzas. \n\
Each person gets {slices_per_person} slices of pizza.\n\
There are {remainder_slices} leftover pieces")

if __name__ == "__main__":
    main()
