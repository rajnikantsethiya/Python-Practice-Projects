#problem
"""You need to build a sequence number printer which can print directly from list which has only names"""

#solution
list = ["Raj", "shell", "suhu", "prach"]

# This uses enumerate which helps in adding indexes to an list

for idx, name in enumerate(list, start=1): # Default start is 0
    print(f"{name}, Your sequence number is {idx}")
