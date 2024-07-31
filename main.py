# Project - Creating a calculator to calculate the area of some common 2D and 3D Shapes

from math import pi # importing pi from math module
import time # importing time module

# Function for calculating the area of a square
def square():
    print("\n*** Area of a Square (2D Shape) ***")
    a = float(input("\nEnter the length of the sides: "))
    area_square = a * a
    print(f"\nArea of this Square is: {area_square} (unit)²")

# Function for calculating the area of a rectangle
def rectangle():
    print("\n*** Area of a Rectangle (2D Shape) ***")
    l = float(input("\nEnter the length: "))
    w = float(input("Enter the width: "))
    area_rectangle = l * w
    print(f"\nArea of this Rectangle is: {area_rectangle} (unit)²")

# Function for calculating the area of a circle
def circle():
    print("\n*** Area of a Circle (2D Shape) ***")
    r = float(input("\nEnter the radius: "))
    area_circle = pi * (r**2)
    print(f"\nArea of this Circle is: {area_circle} (unit)²")

# Function for calculating the area of a triangle
def triangle():
    print("\n*** Area of a Triangle (2D Shape) ***")
    b = float(input("\nEnter the length of the base: "))
    h = float(input("Enter the height: "))
    area_triangle = 1/2 * (b * h)
    print(f"\nArea of this Triangle is: {area_triangle} (unit)²")

# Function for calculating the surface area of a cube
def cube():
    print("\n*** Surface Area of a Cube (3D Shape) ***")
    a = float(input("\nEnter the edge length: "))
    area_cube = 6 * (a**2)
    print(f"\nSurface Area of this Cube is: {area_cube} (unit)²")

# Function for calculating the surface area of a cuboid
def cuboid():
    print("\n*** Surface Area of a Cuboid (3D Shape) ***")
    l = float(input("\nEnter the length: "))
    w = float(input("Enter the width: "))
    h = float(input("Enter the height: "))
    area_cuboid = 2 * ((l*h) + (l*w)+ (h*w))
    print(f"\nSurface Area of this Cuboid is: {area_cuboid} (unit)²")

# Function for calculating the surface area of a sphere
def sphere():
    print("\n*** Surface Area of a Sphere (3D Shape) ***")
    r = float(input("\nEnter the radius of a Sphere: "))
    area_sphere = 4 * pi * (r**2)
    print(f"\nSurface Area of this Sphere is: {area_sphere} (unit)²")

# Function for calculating the surface area of a hemisphere
def hemisphere():
    print("\n*** Surface Area of a Hemisphere (3D Shape) ***")
    r = float(input("\nEnter the radius of a Hemisphere: "))
    area_hemisphere = 3 * pi * (r**2)
    print(f"\nTotal Surface Area of this Hemisphere is: {area_hemisphere} (unit)²")

# Function for calculating the surface area of a cone
def cone():
    print("\n*** Surface Area of a Cone (3D Shape) ***")
    r = float(input("\nEnter the radius of the circular base: "))
    l = float(input("Enter the slant height: "))
    area_cone = pi * r * (r+l)
    print(f"\nSurface Area of this Sphere is: {area_cone} (unit)²")

# Creating the Main Menu of the Program using loop
while True:
    # Printing the Heading
    print("\n------------------------------------------------------------------")
    print("|     ***** Area Calculator for Common 2D & 3D Shapes *****      |")
    print("------------------------------------------------------------------")

    # Taking the the input from user to calculate the area of their desired shapes 
    choice = int(input("\nPress 1 - Square\nPress 2 - Rectangle\nPress 3 - Circle\nPress 4 - Triangle\nPress 5 - Cube\nPress 6 - Cuboid\nPress 7 - Sphere\nPress 8 - Hemisphere\nPress 9 - Cone\nPress 10 - Exit/Quit\n\nEnter your choice: "))

    # Creating Conditions
    if choice<1 or choice>10:
        print("Invalid choice, enter a number between 1 and 10")
    elif (choice==1):
        square()
    elif (choice==2):
        rectangle()
    elif (choice==3):
        circle()
    elif (choice==4):
        triangle()
    elif (choice==5):
        cube()
    elif (choice==6):
        cuboid()
    elif (choice==7):
        sphere()
    elif (choice==8):
        hemisphere()
    elif (choice==9):
        cone()
    elif (choice==10):
        print("\nExiting the program.....\n")
        time.sleep(2)
        break