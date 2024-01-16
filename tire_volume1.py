# Student Name: Israel Akinwumi
# Student ID: 472252522

import math

# Function to calculate tire volume
def calculate_tire_volume(width, aspect_ratio, diameter):
    # Convert width to meters
    wm = width / 1000
    # Calculate volume using the provided formula
    # given v = πw^2a(wa + 2,540d) /10,000,000,000

    # splitting to parts
    top = math.pi * width**2 *aspect_ratio*(width*aspect_ratio + 2540 * diameter) 
    bottom = 10000000000
    volume = top / bottom
    
    return volume

# Get input from user
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate and display the tire volume
tire_volume = calculate_tire_volume(width, aspect_ratio, diameter)
print(f"The volume of the tire is: {tire_volume:.2f} cubic units")
