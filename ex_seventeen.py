#!/usr/bin/python3
""" Exercise Seventeen Blood Alcohol Calculator """

def main():
    """ Prompt for users for variety of factors to assess their Blood Alcohol Content """
    print("Please use \"M\" or \"F\".")
    gender = input("Are you male (M) or female (F)? ")
    rate = .73 if gender.upper() == "M" else .66
    try:
        weight = int(input("How much do you weigh in pounds? "))
        drink_num = float(input("How many drinks have you had? "))
        drink_size = float(input("How many ounces made up the drinks? "))
        alc_perc = (float(input("What was the alcohol percentage of the drinks? ")) / 100)
        time = float(input("How many hours since your last drink? "))
        alc_vol = ((drink_num * drink_size) * alc_perc)
        bac = (alc_vol * 5.14) / (weight * rate) - (.015 * time)
        print(f"Your BAC is {bac:.3f}")
        if bac >= 0.08:
            print("It is not legal for you to drive.")
        else:
            print("It is legal for you to drive.")
    except ValueError:
        print("Please enter a number for weight, drinks, size, percentage, and time.")

if __name__ == "__main__":
    main()
