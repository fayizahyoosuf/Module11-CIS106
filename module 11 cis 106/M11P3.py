# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:29:28 2026

@author: shama
"""

def compute_sales_report(sales):
    # Compute commission based on $100,000 threshold
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05

    # Compute next year's target (5% of sales)
    next_year_target = sales * 0.05

    return commission, next_year_target

def main():
    # Input
    last_name = input("Enter salesperson last name: ")
    sales = float(input("Enter sales amount: "))

    # Process
    commission, next_year_target = compute_sales_report(sales)

    # Output
    print(f"Salesperson Last Name: {last_name}")
    print(f"Commission: ${commission:,.2f}")
    print(f"Next Year's Target: ${next_year_target:,.2f}")

main()