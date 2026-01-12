#Problem
"""This is a kettle boiling story!
if the kettle is ON temp should be less than 33 else show an WARNING
if kettle is not active, display its offline"""

# Solution
kettleStatus = 'active'
temp = 33

if kettleStatus == 'active':
    if temp <= 33:
        print("Kettle is enough hot to make your throat warm.")
    else:
        print("WARNING: Kettle is excessively hot. please switch off!")
else:
    print("kettle is off !")
    