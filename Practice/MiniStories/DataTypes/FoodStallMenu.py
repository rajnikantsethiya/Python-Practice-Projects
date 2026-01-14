#Problem
"""This is Food stall menu
We have menu of 4 items listed below, take user input and tell the prices
tea = 10, poha  = 20, samosa = 25, coffee = 15"""

#Solution
from FoodStallAdmin import itemsList 

foodItems = itemsList
seletion = input(f"Please select your option from {foodItems.keys()}:").lower()

item = foodItems.get(seletion)
match seletion:
    case selection if seletion in foodItems.keys():
        print(f"{seletion} is {foodItems.get(seletion)} repees only !")
    case _:
        print(f"We dont serve {seletion}")
