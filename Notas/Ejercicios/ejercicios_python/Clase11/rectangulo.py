class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)

class Rectangulo():
    def __init__(self, a, b):
        self.a = Punto(a.x, a.y)
        self.b = Punto(b.x, b.y)

    def base(self):
        return abs(self.b.x - self.a.x)
    
    def altura(self):
        return abs(self.b.y - self.a.y)
    
    def area(self):
        return self.base() * self.altura()
    
    def __str__(self):
        return f'Rectangulo({self.a}, {self.b})'
    
    def __repr__(self):
        return f'Rectangulo({repr(self.a)}, {repr(self.b)})'
    
    def mover(self, desplazamiento):    
        self.a.add(desplazamiento.x)
        self.b.add(desplazamiento.y)

    def rotar(self):
        centro_x = (self.a.x + self.b.x) / 2
        centro_y = (self.a.y + self.b.y) / 2
        ancho = self.base()
        alto = self.altura()
        self.a.x = centro_x - alto / 2
        self.a.y = centro_y - ancho / 2
        self.b.x = centro_x + alto / 2
        self.b.y = centro_y + ancho / 2
        