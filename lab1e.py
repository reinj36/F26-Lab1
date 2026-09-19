
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 19/9/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.

quantity = 3.56

# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.

stock = 4.27

# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.

multiplicationResult = "%13f" % (quantity * stock) # 9 (total # of characters for product) 
                                                   # + 4 (# of characters for spaces) = 13
print(multiplicationResult)

# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting.

multiplicationResult = "%12.2f" % (quantity * stock) # 5 (total # of character for product)
                                                     # + 7 (# of characters for spaces) = 12
print(multiplicationResult)

