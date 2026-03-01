class Paint:
    # constructor 
    def __init__(self, color, brush):
        self.color = color
        self.brush = brush
    
    def create(self):
        print(f"I am painting with {self.color} color and a {self.brush} brush !")

p1 = Paint('Blue', "Medium")
print(p1.create())