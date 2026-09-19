
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 19/9/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1d.py

#TO-DO 1:
#	Create a variable called "name" and assign it the value of your name.
# Use the string method .upper() to convert the name to upper case.
# Create another variable called “age”, the value of “age” should be your age
# The script, when executed, should print out "How are you yourname? Happy xxth birthday!" To print this output use .format() method. 

#variables
name = "Reina"
name = name.upper() #change name value to uppercase
age = 18

#print out formatted message using name and age
print("How are you {}? Happy {}th birthday!".format(name, age))


#TO-DO 2:
# Create a variable called "words".
# The value of words should be "The quick brown fox jumps over the lazy dog".
# Use indexing to return the first and 17th charecters of "words" to the user.

#variables
words = "The quick brown fox jumps over the lazy dog"

#return first and 17th character of "words" to user
print("\nFirst character: {}\nSecond character: {}".format(words[0], words[16]))

#TO-DO 3:
# Use negative indexing to return the words "jumps" and "quick" from "words" to the user.

#return specified words with negative indexing
print("\n{}, {}".format(words[-23:-18], words[-39:-34]))

#TO-DO 4:
# Use slicing to retun everything between index 2-15 to the user.
# Print "uick brown foxs ju" from "words".

#return "e quick brown " to user (chars at index 2-15)
print("\n" + words[2:16])

#print "uick brown foxs ju" using indexes
print("\n" + words[5:19] + words[24:26] + words[20:22])
