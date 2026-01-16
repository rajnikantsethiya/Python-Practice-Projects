# Simple named function

def Hello():
    print("I am a simple function !")

# Separation and readability
def findPhone():
    print("Phone found !")

def chargePhone():
    findCharger()
    findPhone()
    plugStart()
    print("Your phone is charging.")

def findCharger():
    print("Charger found !")

def plugStart():
    print("Started plug !")


# Scope (named, global, nonlocal)

def main():
    type = "phone"
    def sub():
        type = "ios"
        print(type) # ios
    print(type) # phone

def main():
    type = "phone"
    def sub():
        nonlocal type # Modifying the value of its immediate parent variable
        type = "ios"
        print(type) # ios
    print(type) # ios


type = "coffee"
def main():
    type = "tea"
    def sub():
        # nonlocal type # This will give error to global for not defined/binded, meaning only one scope can be defined.
        global type
        type = "lemon"
        print(f"Sub: {type}") # lemon
    sub()
    print(f"Main: {type}") # tea


main()
print(f"Global: {type}") # lemon