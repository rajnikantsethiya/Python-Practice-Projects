#Problem
"""You need to build Bill printing machine, with the customer name and bill amount."""

#solution
customerList = ["Raj", "uday", "john", "Ash"]
BillAmounts = ["100", "300", "5000", "1212"]

# This solution uses Zip to combine 2 lists and make it like a list of tuple

for name, amount in zip(customerList, BillAmounts):
    print(f"{name}, Your Bill amount is {amount} !")