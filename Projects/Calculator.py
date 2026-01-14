def Calc():
    listOfOperation = ("add", "sub", "multiply", "divide")
    operation = input("what would you like to perform (add/sub/multiply/divide):").lower()
    firstValue = int(input("Please enter the first value:"))
    secondValue = int(input("Please enter the second value:"))

    if (firstValue and secondValue and operation in listOfOperation):
        match operation:
            case "add":
                res = firstValue + secondValue
            case "sub":
                res = firstValue - secondValue
            case "multiply":
                res = firstValue * secondValue
            case "divide":
                res = firstValue / secondValue
            case _:
                res = "Please select a valid operation !"
        return f"The result is {res}"
    else:
        return f"Input options are invalid. Please try again !"

print(Calc())