# There are few ways to access the base class.
# 1. Explicitly accessing
# 2. Super keyword
class Paint:
    def __init__(self, color):
        self.color = color
        print('Paint:', color)

# explicitly accessing inherited class and assigning new ones to cureent constructor
class Coloring(Paint):
    def __init__(self, color, brush):
        Paint.__init__(self, color)
        self.brush = brush
        print('Coloring:', color, brush)

# Super keyword does all the job of getting previous ones
class Varnish(Paint):
    def __init__(self, color, brush):
        super().__init__(color)
        self.brush = brush
        print('Varnish:', color, brush)

Paint('Red')
Varnish('Green', 'Broad')
Coloring('Blue', 'Thin')
