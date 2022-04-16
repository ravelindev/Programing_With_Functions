"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
heart_rate = 220
input_age = int(input("Please enter your age: "))
heart_max = heart_rate - input_age
print(f"Your maximum heart rate is: ", heart_max)
print(f"When exercising to strengthen your heart, you should keep your bheart rate between {int(65 * heart_max / 100)} and {int(85 * heart_max / 100)} of your heart's maximum rate.")