#!/usr/bin/python3
""" Exercise Seven Area of a Rectangular Room """

def main():
    """ Convert Square Feet to Square Meters """
    room_length = input("What is the length of the room in feet?\n> ")
    room_width = input("What is the width of the room in feet?\n> ")
    print(f"You entered dimensions of {room_length} feet by {room_width} feet.")
    room_square_feet = int(room_length) * int(room_width)
    meter_conversion = ((room_square_feet) * 0.09290304)
    print(f"The area is\n{room_square_feet} square feet\n{meter_conversion} square meters")

if __name__ == "__main__":
    main()
