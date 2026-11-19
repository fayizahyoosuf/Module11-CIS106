# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:05:43 2026

@author: shama
"""

def compute_discount(qty, unit_price, rate, return_values):
    extended_price = qty * unit_price
    return_values[0] = extended_price * rate
    return_values[1] = extended_price - return_values[0]

def main():
    # Declare variables
    results = [0.0, 0.0]

    # Input
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the unit price: "))
    discount_rate = float(input("Enter the discount rate (e.g. 0.10 for 10%): "))

    # Process
    compute_discount(quantity, price, discount_rate, results)
    discount_amount = results[0]
    discounted_price = results[1]

    # Output
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ${price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")

main()
