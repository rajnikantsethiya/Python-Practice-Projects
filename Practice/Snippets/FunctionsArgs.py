def Main(first, second, third):
    print(first, second, third)

Main(1,2,3)

# These are arguments and kwargs (key:value arguments)
def Main(regularParam, *menu, **menuItems): 
    print(f" Menu Choices: {menu} and items {menuItems} with regular sauces {regularParam}" )


Main("Chilli & Tomato", "indian", "mexican", "italian", indian = "paneer tikka", mexican = "samsaraa" )

    
