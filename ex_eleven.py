#!/usr/bin/python3
""" Exercise Eleven Currency Conversion """
from decimal import ROUND_UP, getcontext, Decimal

def main():
    """ Exchange Rate Function """
    amnt_from = Decimal(input("How many euros are you exchanging?\n> "))
    rate_from = Decimal(input("What is the current exchange rate in euros?\n> "))
    amnt_to = Decimal(amnt_from * (rate_from / 100))
    getcontext().prec = 3 
    getcontext().rounding = ROUND_UP
    print(f"{amnt_from:.0f} euros at an exchange rate of\
 {rate_from:.2f} is {amnt_to:.2f} U.S. dollars.")

if __name__ == "__main__":
    main()
