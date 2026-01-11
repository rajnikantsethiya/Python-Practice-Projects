def Calc(val1, val2, operation):
    operations = ("+", "-","*","/")
    result = None
    if operation in operations:
        if (operation == "+"):
            result = val1 + val2
        if (operation == "-"):
            result = val1 - val2
        if (operation == "*"):
            result = val1 * val2
        if (operation == "/"):
            result = val1 / val2
    else:
        return result
    return f"Output for the operation {operation} is {result}"

print(Calc(2,5,"="))
    