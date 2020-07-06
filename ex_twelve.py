#!/usr/bin/python3
""" Exercise Twelve Computing Simple Interest """
from decimal import *
def main():
    """ Computing Interest through Decimal """
    principal = Decimal(input("Enter the principal: "))
    roi = Decimal(input("Enter the rate of interest: "))
    time = Decimal(input("Enter the number of years: "))
    result = Decimal((principal * (1 + ((roi / 100) * time))))
    result = Decimal(result).quantize(Decimal('1.00'), rounding=ROUND_UP)
    print(f"After {time} years at {roi}%, the investment will be worth ${result}.")

if __name__ == "__main__":
    main()
