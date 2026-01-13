#Problem
"""Create a delivery fee calculator based on the cart value.
if order value is more than 200, delivery fee is 0
if less than required value, its 30 INR"""

#Solution
cartValue = 100
# This is an example of ternary operator with if else
fees = 0 if cartValue < 200 else 30
print(f"Your delivery fee is: {fees}")