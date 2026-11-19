# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:39:38 2026

@author: shama
"""

total = 0.0
tax = 0.0

def compute_total_and_tax(qty, unit_price):
    global total, tax
    total = qty * unit_price
    tax = total * 0.07

def main():
    # Input
    quantity = int(input("Enter the quantity: "))
    unit_price = float(input("Enter the unit price: "))

    # Process (Updates global variables total and tax directly)
    compute_total_and_tax(quantity, unit_price)

    # Output
    print(f"Total: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")

main()