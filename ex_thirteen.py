#!/usr/bin/python3
""" Exercise Thirteen Determining Compound Interest """
from decimal import *

def main():
    """ Determining Compound Interest """
    principal = Decimal(input("Enter the principal: "))
    roi = Decimal(input("Enter the rate of interest: "))
    time = Decimal(input("Enter the number of years: "))
    comp_num = Decimal(input("Enter the number of times the interest\
 compounded per year: "))
    num_of_comps = (comp_num * time)
    result = Decimal((principal * ((1 + ((roi / 100) / comp_num)) ** num_of_comps)))
    result = Decimal(result).quantize(Decimal('1.00'), rounding=ROUND_UP)
    print(f"After {time} years at {roi}%, the investment will be worth ${result}.")

if __name__ == "__main__":
    main()
