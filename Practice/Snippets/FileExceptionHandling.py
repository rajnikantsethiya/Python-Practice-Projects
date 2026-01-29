# Basic way of ediding a file
# file = open("note.txt", "w")
# file.write("I am happy !")
# file.close()

# File editing with "with", No need to close the file it automatically does.
try:
    with open("note.txt", "x") as f:
        f.write("I am happiest !!")
except:
    raise FileExistsError("File doesnt exists")
finally:
    print("Its done !")

# For deleting the file.
# import os
# os.remove("note.txt")