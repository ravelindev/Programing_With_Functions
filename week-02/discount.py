# Copyright 2022, Rudt Ravelin. All rights reserved.

"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""
# Let's start by importing the date and time modules
from datetime import datetime

# Let's define the discount rate and the sales rate
discount_rate = 0.10
sales_rate = 0.06

# Let's get the subtotal from the user
subtotal = float(input("Please enter the subtotal: "))
#Let's get the date from our computer
# The current date and time
current_date_and_time = datetime.now()

# Let's get the weekday from the current date
weekday = current_date_and_time.weekday()

#weekday = 3
 
# Now Let's check if the weekday is Tuesday or Wednesday
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    # If the subtotal is greater than $50 and the weekday is Tuesday or Wednesday,
    # we will apply the discount
    discount = round(subtotal * discount_rate,2)
    # We will also apply the sales tax
    sales_tax = (subtotal - discount) * sales_rate
    # We will then calculate the total
    total = subtotal + sales_tax - discount
    # Let's print the results
    print()
    print("Discount: $", format(discount, ".2f"))
    print("Sales Tax: $", format(sales_tax, ".2f"))
    print("Total: $", format(total, ".2f"))
else:
    # If the subtotal is less than $50 or the weekday is not Tuesday or Wednesday,
    # we will not apply the discount
    print()
    print("No discount applied")
    # We will also apply the sales tax
    sales_tax = subtotal * sales_rate
    # We will then calculate the total
    total = subtotal + sales_tax
    # Let's print the results
    print("Sales Tax: $", format(sales_tax, ".2f"))
    print("Total: $", format(total, ".2f"))
