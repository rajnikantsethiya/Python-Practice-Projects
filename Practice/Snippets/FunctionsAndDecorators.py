def Main(first, second, third):
    print(first, second, third)

Main(1,2,3)

# These are arguments and kwargs (key:value arguments)
def Main(regularParam, *menu, **menuItems): 
    print(f" Menu Choices: {menu} and items {menuItems} with regular sauces {regularParam}" )


Main("Chilli & Tomato", "indian", "mexican", "italian", indian = "paneer tikka", mexican = "samsaraa" )

def positionOnly(name, age, skill, /):
    print(name, age, skill)

def keywordOnly(*, name, age):
    print(name, age)

def unknownNoOfArgs(*itmes):
    print(itmes) # prints tuple

def unknownNoOfKeyPairArgs(**items):
    print(items) # prints dict with key pair

positionOnly("raj", 33, "code")
keywordOnly(name="raj", age=33)
unknownNoOfArgs("Raj", 33, 22, 33,55, False)
unknownNoOfKeyPairArgs(name="raj", age=33, hobby="code", drinks=False)

## Decorators
# without args
def talk(func):
    def inner():
        return func().upper()
    return inner
@talk
def subFunc():
    return("life is injoy !")

print(subFunc())

# with args
def talk(n):
    def talk(func):
        def inner():
            if n > 18:
                return func().upper()
            else: 
                return func()
        return inner
    return talk
@talk(18)
def subFunc():
    return("life is injoy !")

print(subFunc())

        
    
