# Author: Antonio Loureiro Dunch
# GitHub username: aloureirodunch
# Date: April 16th, 2026
# Description: Calculator to determine the area, perimeter, and diagonal of a given rectangle.

length = input("Enter the length of a rectangle please: ")
width = input("Now enter the width of the rectangle:")

length = float(length)
width = float(width)

area = round(length * width, 1)
print(f"The area of the rectangle is {area} units.")

perimeter = round((length + length + width + width), 1)
print(f"The perimeter of the rectangle is {perimeter} units.")

diagonal = round(((length**2 + width**2) ** (1/2)), 2)
print(f"The diagonal of the rectangle is {diagonal} units.")