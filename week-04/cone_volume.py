"""Compute and print the volume of a right circular cone."""

# Import the standard math module so that
# math.pi can be used in this program.
import math # import the standard math module so that

def main(): # 
    # Call the cone_volume function to compute
    # the volume of an example cone.
    ex_radius = 2.8 # radius of the example cone
    ex_height = 3.2 # height of the example cone
    ex_vol = cone_volume(ex_radius, ex_height) # volume of the example cone

    # Print several lines that describe this program.
    print("This program computes the volume of a right")  
    print("circular cone. For example, if the radius of a")
    print(f"cone is {ex_radius} and the height is {ex_height}") 
    print(f"then the volume is {ex_vol:.1f}")
    print()

    # Get the radius and height of the cone from the user.
    radius = float(input("Please enter the radius of the cone: ")) # get the radius of the cone from the user
    height = float(input("Please enter the height of the cone: ")) # get the height of the cone from the user

    # Call the cone_volume function to compute the volume
    # for the radius and height that came from the user.
    vol = cone_volume(radius, height) # volume of the cone

    # Print the radius, height, and
    # volume for the user to see.
    print(f"Radius: {radius}") # print the radius of the cone
    print(f"Height: {height}") # print the height of the cone
    print(f"Volume: {vol:.1f}") # print the volume of the cone


def cone_volume(radius, height): # compute the volume of a cone
    """Compute and return the volume of a right circular cone."""
    volume = math.pi * radius**2 * height / 3 # compute the volume of the cone
    return volume # return the volume of the cone


# Start this program by
# calling the main function.
main() 