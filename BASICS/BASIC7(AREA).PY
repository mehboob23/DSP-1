import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")
#.2f means only 2 number after decimal point
