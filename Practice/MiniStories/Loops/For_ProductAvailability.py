#problem
"""You need to build a system which tells about product availbility based on the existing list
if It doesnt exist, break the loop and if its out of stock just skip it"""

#solution

list = [("pasta", "designing"),("tea", "available"),  ("coffee", "out of stock"), ("maggi", "unavailable")]

for item, status in list:
    if (status == "available" or "unavailable" or "out of stock"):
        print(f"{item} is {status} to serve")
        break
else:
    print(f"This is out of scope.")
