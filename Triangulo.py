import math

class Triangulo:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
            pass
        else:
            if self.a == self.b or self.a == self.c:
                return 'isósceles'
            else:
                return 'escaleno'
    
    def retangulo(self):
        lista = []
        lista.append(self.a)
        lista.append(self.b)
        lista.append(self.c)
        lista.sort()
        c1 = lista[0]
        c2 = lista[1]
        hip = lista[2]
        if hip == math.sqrt((c1**2) + (c2**2)):
            return True
        else:
            return False
    
    def semelhantes(self,triangulo):
        l1 = []
        l1.append(self.a)
        l1.append(self.b)
        l1.append(self.c)
        l1.sort()
        l2 = []
        l2.append(triangulo.a)
        l2.append(triangulo.b)
        l2.append(triangulo.c)
        l2.sort()
        a1 = l1[0]
        a2 = l1[1]
        a3 = l1[2]
        b1 = l2[0]
        b2 = l2[1]
        b3 = l2[2]
        c1 = a1 / b1
        c2 = a2 / b2
        c3 = a3 / b3
        if c1 == c2 and c2 == c3:
            return True
        else:
            return False
        
        
