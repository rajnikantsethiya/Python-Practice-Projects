# Comprehensions are just add on methods of memory and code optimizations
# [expression for in iterable if condition]
# list comprehensions
from turtle import colormode


colors = ['red', 'green', 'yellow', 'blue']
redColor = [color for color in colors if color == 'red']
print(redColor)

# set comprehensions
colors = {'red', 'green', 'blue', 'pink'}
pinkColor = {color for color in colors if color == 'pink'}
print(pinkColor)

# dict comprehension
colors = {
    'red': ['maroon', 'beige'],
    'pink': ['megenta', 'dark', 'light'],
    'green': ['flower', 'color', 'signal']
}
uniqueColorType = { colormode for types in colors.values() for colormode in types if colormode == 'flower' }
print(uniqueColorType)

arts = {
    "frame": 100,
    "dolls": 200,
    "brushes": 500
}
pricingWithin10 = { item:price / 100 for item, price in arts.items()}
print(pricingWithin10)

# generator comprehensions

bikesBrands = ['fz', 'tvs', 'hero', 'honda']
# This is for memory efficience which gets executed in chunks so that it doesnt consume memory in one shot
sortedItems = sorted(brand for brand in bikesBrands)
print(sortedItems)


