import math

class Triangulo_ret:
    
    def tri_ret(c1, c2, h):
        if h == math.sqrt((c1**2)+(c2**2)):
            return True
        else:
            return False

    if __name__ == '__main__':
        c1 = float(input("Valor do cateto 1: "))
        c2 = float(input("Valor do cateto 2 :"))
        h = float(input("Valor da hipotenusa :"))
        print(tri_ret(c1, c2, h))
