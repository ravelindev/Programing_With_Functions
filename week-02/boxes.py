# This is a programm that will ask a suser to enter some numbers for items and boxes.
# It will calculate the total boxes need to pack the items

#inport the math module
import math

#aks the user to enter the number of items
items = int(input("Enter the number of items: "))
#ask the user to enter the number of boxes
boxes = int(input("Enter the number of boxes: "))

print()
#calculate the total boxes needed
number_of_boxes = math.ceil(items/boxes)
print()

#display the total boxes needed
print (f"For {items} items, packing {boxes} items in each box, you will need {number_of_boxes} boxes")