#!/usr/bin/python3
""" Tax Calculator """
from decimal import Decimal, getcontext, ROUND_UP
def main():
    """ Tax Calculation based on Amount and Wisonsin State Residence """
    order_amt = Decimal(input("What is the order amount? "))
    state = input("What is the state? ")
    total = order_amt
    if state == "WI":
        total = (order_amt * Decimal('1.055'))
    tax = (total - order_amt)
    total = Decimal(total).quantize(Decimal('.00'), rounding=ROUND_UP)
    getcontext().prec = 3
    getcontext().rounding = ROUND_UP
    print(f"The subtotal is ${order_amt:.2f}\nThe tax is ${tax:.2f}.\nThe total is ${total:.2f}.")

if __name__ == "__main__":
    main()
