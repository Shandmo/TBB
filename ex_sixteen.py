#!/usr/bin/python3
""" Exercise Sixteen Legal Driving Age """

def main():
    """ Test user's age using ternary operator """
    try:
        age = int(input("What is your age? "))
        state = "You are old enough to legally drive." if age >= 16\
        else "You are not old enough to legally drive."
        if age < 0:
            print("Please input a valid age.")
        else:
            print(state)
    except ValueError:
        print("Please only input whole numbers.")

if __name__ == "__main__":
    main()
