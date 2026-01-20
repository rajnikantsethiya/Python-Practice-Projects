class Main:
    print("This is a simple class")

instance = Main() # creating object of a class
print(instance, type(instance), type(Main))

class Paint:
    color = 'red'
    print(color)

P1 = Paint()
P1.color = 'blue'

print('After change, P1 value', P1.color)
print('After change, Paint value', Paint.color)