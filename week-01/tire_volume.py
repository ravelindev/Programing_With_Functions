import math
width = float(input("Please enter the tire width in mm (ex 205): "))
ratio = float(input("Please enter aspect of the tire (ex 60): "))
diameter = float(input("Please enter diameter of the wheel in inches (ex 15): "))
# v = π w2 aw a + 2,540 d /10,000,000,000
volume = (math.pi * float(width) * float(width) * float(ratio) * (float(width) * float(ratio) + 2540 * diameter)) / 10000000000

#print(f"The approximate volume is: {math.pi * (int(width) / 1000) * (int(ration) / 100) * (int(diameter) / 100)}")
print(f"The approximate volume is: {volume:.2f}")