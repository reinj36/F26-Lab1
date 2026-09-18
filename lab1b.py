# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 18/9/2026
# Purpose: Use arithmetic in python.
# Usage: python3 lab1b.py

# TO-DO 1:
#	Create a variable called "num1", take its value from user.
#	Create another variable called "num2" and take its value from user. 
# Convert the values to integers using int() function

#get user input
print()
num1 = input("Enter a value: ")
num2 = input("Enter a value again: ") 

num1 = int(num1)
num2 = int(num2)


# TO-DO 2:
# Perform all arithmetic oeprations as outlined in the description in README.md file, and print in the required format.

print() #add a space between input and results for formatting

#print results
print("num1 + num2 = " + str(num1 + num2))
print("num1 - num2 = " + str(num1 - num2))
print("num1 * num2 = " + str(num1 * num2))
print("num1 ** num2 = " + str(num1 ** num2))
print("num1 / num2 = " + str(num1/num2))
print("num1 // num2 = " + str(num1//num2))
print("num1 % num2 = " + str(num1%num2))
