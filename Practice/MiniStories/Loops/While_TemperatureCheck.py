#problem 
"""You need to build a temperature check sysstem which indicates when the water is ready to boil"""

#solution
temp = 40

while temp < 100:
    print(f"Current temperature is {temp}")
    temp += 20

print(f"Water is ready to boil")