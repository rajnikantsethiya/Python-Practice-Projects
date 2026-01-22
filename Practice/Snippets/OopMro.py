# Multiple inheritance or MRO (Method resolution order) is where method decides 
# which common method is supposed to be executed

class Eat:
    label = "Eat"

class Code(Eat):
    label = "Code"

class Sleep(Eat):
    label = "Sleep"

class Repeat(Code, Sleep):
    pass

R1 = Repeat().label

# As we have a common label in all the 3 class, 
# Now when Repeat class try to access common item across the inherited classes, 
# It ll print the first inherited class from Repeat which is Code
print(R1)
# Dunder MRO will print the hierarchy
print(Repeat.__mro__)