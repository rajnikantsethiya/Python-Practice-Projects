# Static methods

class Paint:
    @staticmethod
    def coloring(color, brush):
        print(f"I am coloring with {color} color and {brush} brush!")

# usual way is creating an object and call method
# P1 = Paint()
# P1.coloring('red', 'thin')

# We can use static method decorator to which helps us to 
# call methods direclty without creating an object.
Paint.coloring('red', 'thin')

# Classmethod - 
# This is being used for extenting the constructor and it has access to cls which is a reference access of entire class.

class Main:
    def __init__(self, color, brush):
        self.color = color
        self.brush = brush
    
    @classmethod
    def from_dict(cls, paintData):
        return cls(paintData["color"], paintData["brush"])
    
    @classmethod
    def from_string(cls, paintData):
        color, brush = paintData.split(',')
        return cls(color, brush)


M1 = Main.from_dict({"color":"red", "brush":"thin"})
print(M1.__dict__)
M2 = Main.from_string('Blue,medium')
print(M2.__dict__)