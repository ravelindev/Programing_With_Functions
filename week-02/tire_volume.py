# inport math
import math
# Let's import the datetime module
from datetime import datetime
# Let's call the datetime.now() function
current_date_and_time = datetime.now()
#Let's print only the date part of the current date and time
# print(f"{current_date_and_time:%Y-%m-%d}")
# # Let's call the weekday function
# weekday = current_date_and_time.weekday()
# print(f"Today is: {weekday}")
width = float(input("Please enter the tire width in mm (ex 205): "))
ratio = float(input("Please enter aspect of the tire (ex 60): "))
diameter = float(input("Please enter diameter of the wheel in inches (ex 15): "))
# v = π w2 aw a + 2,540 d /10,000,000,000
volume = (math.pi * float(width) * float(width) * float(ratio) * (float(width) * float(ratio) + 2540 * diameter)) / 10000000000

#print(f"The approximate volume is: {math.pi * (int(width) / 1000) * (int(ration) / 100) * (int(diameter) / 100)}")
print(f"The approximate volume is: {volume:.2f} liters")

with open("volumes.txt", "at") as file:
    file.write(f"{current_date_and_time:%Y-%m-%d}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}\n")
print()
asking_user_to_buy = input("Do you want to buy the tire? (y/n): ")
if asking_user_to_buy == "y":
    print("Thank you for your purchase")
else:
    print("Thank you for your visit")
phone = (input("Please enter your phone number: "))
with open("volumes.txt", "at") as file:
        file.write(f"This is your Phone Number: {phone}\n")
print("The volume and your phone has been saved in our database")