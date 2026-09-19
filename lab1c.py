
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 18/9/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
# Create a variable called 'radius' and take its value form user.
# Convert the variable to integer using int()
# use the contant pi form math module and compute the area of the circle using the variable 'radius'

#import math module
import math

#get user input and convert it to int
r = input("Enter radius: ")
r = int(r)

#calculate area and return in formatted message
area = math.pi * r**2
print("Area: {}".format(area))
