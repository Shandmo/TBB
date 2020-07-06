#!/usr/bin/python3
""" Exercise Ten Self-Checkout Challengs Version """
# Challenge One - Ensure that price and quantities are entered as numeric values.
# Don't allow user to proceed if value entered is not numeric.
# Challenge Two - Allow indeterminate number of items to be entered.
# Tax and Total are computed when there are no more items to entered.

def main():
    """ Self Checkout System """
    prices = {}
    tax = 0.055
    print("Enter the item prices(s), then press \"q\" to quit.")
    while True:
        item_price = input("Price: ")
        item_num = input("Quantity: ")
        # Checking if user input is numeric.
        try:
            item_price = float(item_price)
            item_num = float(item_num)
            prices[item_price] = item_num
        except ValueError:
            if item_price or item_num == "q":
                break
            else:
                print("Please only enter numeric values or press \"q\" to quit.")
    sub_total = 0
    for k, v in prices.items():
        sub_total += (k * v)
    sub_total = round(sub_total, 2)
    tax_amnt = round(sub_total * tax, 2)
    total = round(sub_total + tax_amnt, 2)
    print(f"Subtotal: ${sub_total:.2f}\nTax: ${tax_amnt:.2f}\nTotal: ${total:.2f}")

if __name__ == "__main__":
    main()
