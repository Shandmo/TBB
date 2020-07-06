#!/usr/bin/python3
""" Exercise Nine Paint Calculator """
import math
def main():
    """ Calculates gallons of paint needed based on square footage """
    gallon_coverage = 350
    rm_len = input("What is the length of the room in feet?\n> ")
    rm_width = input("What is the width of the room in feet?\n> ")
    sq_area = (int(rm_len) * int(rm_width))
    result = math.ceil(sq_area / gallon_coverage)
    # Handle plurality and zero sum cases.
    if result == 1:
        print(f"You will need to purchase {result} gallon of paint.")
    elif result > 1:
        print(f"You will need to purchase {result} gallons of paint.")
    else:
        print(f"Your square footage equates to {result}, no paint needed!")

if __name__ == "__main__":
    main()
