class PaintBase:
    def __init__(self, color):
        self.color = color
    
    def create(self):
        print(f'I am creating a painting with {self.color} color !')

# inheritance
class CreatePortrait(PaintBase):
   def varnish(self):
        print(f'Varnish the painting post coloring with {self.color}')

p2 = CreatePortrait('Red')
p2.create()

class BlowAir:
    portrait = CreatePortrait

B1 = BlowAir()
B1.portrait('Green').create()
B1.portrait('Green').varnish()