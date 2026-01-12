#Problem
"""A Dashboard or list of products where admin can add or remove the items from menu
updated list should be used in FoodStallMenu.py"""

#Solution
itemsList = dict({
    "tea": 10,
    "coffee": 15,
    "poha": 20,
    "samosa": 25
})
def Menu():
    
    itemToAdd = input("Please enter item to add in menu: ").lower()
    itemPrice = int(input("Please enter price of the item you added: "))

    itemsList.update({itemToAdd: itemPrice})

    print(f"Updated menu: {itemsList}")
    return itemsList

# This is to skip the execution while imported in other files or modules. Until its directly called it won't execute
if __name__ == "__main__":
    Menu()
